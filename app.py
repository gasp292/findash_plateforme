"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║              FINANCIAL DASHBOARD — 10-Year Asset Performance Tracker             ║
║              Streamlit · yfinance · pandas                                       ║
║              Deploy-ready: Streamlit Community Cloud / Hugging Face              ║
╚══════════════════════════════════════════════════════════════════════════════════╝

Author  : AI-generated, production-grade
Version : 1.1.0  — adds watchlist persistence (CSV) + Claude markdown export
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG  (must be the very first Streamlit call)
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FinDash — 10-Year Tracker",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS  (dark, professional, no purple-gradient clichés)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Global ── */
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'IBM Plex Sans', sans-serif;
        background-color: #0d0f14;
        color: #d4dbe8;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background-color: #111520;
        border-right: 1px solid #1e2535;
    }
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stMarkdown p {
        color: #8899bb !important;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* ── Metric cards ── */
    [data-testid="stMetric"] {
        background: #151925;
        border: 1px solid #1e2d45;
        border-radius: 8px;
        padding: 16px 20px;
    }
    [data-testid="stMetricLabel"] { color: #6e84a3 !important; font-size: 0.75rem; }
    [data-testid="stMetricValue"] {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 1.5rem !important;
        color: #e8eef8 !important;
    }
    [data-testid="stMetricDelta"] { font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem; }

    /* ── Dataframe / table ── */
    [data-testid="stDataFrame"] { border: 1px solid #1e2535; border-radius: 8px; }

    /* ── Dividers / headers ── */
    h1, h2, h3 { font-family: 'IBM Plex Mono', monospace; color: #c8d8f0; }
    hr { border-color: #1e2535; }

    /* ── Buttons in sidebar (asset remove) ── */
    .remove-btn button {
        background: transparent;
        border: 1px solid #2a3550;
        color: #c0392b;
        border-radius: 4px;
        padding: 2px 8px;
        font-size: 0.75rem;
        cursor: pointer;
    }
    .remove-btn button:hover { border-color: #c0392b; }

    /* ── Tab strip ── */
    button[data-baseweb="tab"] { font-family: 'IBM Plex Mono', monospace; font-size: 0.82rem; }

    /* ── Positive / negative color helpers ── */
    .pos { color: #27ae60; font-weight: 600; }
    .neg { color: #e74c3c; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# ASSET DATABASE  (name → ticker mapping)
# ─────────────────────────────────────────────────────────────────────────────
ASSET_DB: dict[str, str] = {
    # ── US Equities ──────────────────────────────────────────────────────────
    "Apple Inc. (AAPL)":                    "AAPL",
    "Microsoft Corp. (MSFT)":               "MSFT",
    "Alphabet / Google (GOOGL)":            "GOOGL",
    "Amazon.com Inc. (AMZN)":              "AMZN",
    "NVIDIA Corp. (NVDA)":                  "NVDA",
    "Meta Platforms (META)":                "META",
    "Tesla Inc. (TSLA)":                    "TSLA",
    "Berkshire Hathaway B (BRK-B)":        "BRK-B",
    "JPMorgan Chase (JPM)":                 "JPM",
    "Visa Inc. (V)":                        "V",
    "Johnson & Johnson (JNJ)":              "JNJ",
    "Exxon Mobil (XOM)":                    "XOM",
    "UnitedHealth Group (UNH)":             "UNH",
    "Procter & Gamble (PG)":               "PG",
    "Home Depot (HD)":                      "HD",
    "Mastercard (MA)":                      "MA",
    "Netflix Inc. (NFLX)":                  "NFLX",
    "Salesforce (CRM)":                     "CRM",
    "Adobe Inc. (ADBE)":                    "ADBE",
    "PayPal Holdings (PYPL)":              "PYPL",
    "Intel Corp. (INTC)":                   "INTC",
    "Advanced Micro Devices (AMD)":        "AMD",
    "Palantir Technologies (PLTR)":        "PLTR",
    "Coinbase Global (COIN)":              "COIN",
    # ── European Equities ────────────────────────────────────────────────────
    "LVMH Moët Hennessy (MC.PA)":          "MC.PA",
    "Airbus SE (AIR.PA)":                   "AIR.PA",
    "TotalEnergies (TTE.PA)":              "TTE.PA",
    "ASML Holding (ASML.AS)":              "ASML.AS",
    "SAP SE (SAP.DE)":                     "SAP.DE",
    "Siemens AG (SIE.DE)":                 "SIE.DE",
    "Nestlé SA (NESN.SW)":                 "NESN.SW",
    "Roche Holding (ROG.SW)":              "ROG.SW",
    "Novo Nordisk (NVO)":                   "NVO",
    "Shell PLC (SHEL)":                     "SHEL",
    # ── Indices ──────────────────────────────────────────────────────────────
    "S&P 500 (^GSPC)":                      "^GSPC",
    "NASDAQ Composite (^IXIC)":            "^IXIC",
    "Dow Jones (^DJI)":                     "^DJI",
    "CAC 40 (^FCHI)":                       "^FCHI",
    "DAX 40 (^GDAXI)":                      "^GDAXI",
    "FTSE 100 (^FTSE)":                     "^FTSE",
    "Nikkei 225 (^N225)":                   "^N225",
    "Russell 2000 (^RUT)":                  "^RUT",
    "VIX Volatility (^VIX)":               "^VIX",
    # ── Cryptocurrencies ─────────────────────────────────────────────────────
    "Bitcoin (BTC-USD)":                    "BTC-USD",
    "Ethereum (ETH-USD)":                   "ETH-USD",
    "BNB (BNB-USD)":                        "BNB-USD",
    "Solana (SOL-USD)":                     "SOL-USD",
    "XRP (XRP-USD)":                        "XRP-USD",
    "Cardano (ADA-USD)":                    "ADA-USD",
    "Dogecoin (DOGE-USD)":                  "DOGE-USD",
    # ── ETFs ─────────────────────────────────────────────────────────────────
    "SPDR S&P 500 ETF (SPY)":              "SPY",
    "Invesco QQQ Trust (QQQ)":             "QQQ",
    "iShares MSCI World (URTH)":           "URTH",
    "Vanguard Total Market (VTI)":         "VTI",
    "ARK Innovation ETF (ARKK)":          "ARKK",
    "Gold ETF (GLD)":                      "GLD",
    # ── Commodities ──────────────────────────────────────────────────────────
    "Gold Futures (GC=F)":                  "GC=F",
    "Silver Futures (SI=F)":               "SI=F",
    "Crude Oil WTI (CL=F)":               "CL=F",
    "Natural Gas (NG=F)":                  "NG=F",
}

# Sorted display labels for the selectbox
ASSET_LABELS = [""] + sorted(ASSET_DB.keys())

# ─────────────────────────────────────────────────────────────────────────────
# PERSISTENCE — Watchlist on disk (CSV)
# ─────────────────────────────────────────────────────────────────────────────
WATCHLIST_DIR = Path("user_data")
WATCHLIST_FILE = WATCHLIST_DIR / "watchlist.csv"


def load_watchlist() -> list[str]:
    """
    Read saved asset labels from CSV. Returns empty list on missing/corrupt file.
    Filters out any labels that no longer exist in ASSET_DB (asset retired).
    """
    try:
        if WATCHLIST_FILE.exists():
            with WATCHLIST_FILE.open("r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
                return [lbl for lbl in lines if lbl in ASSET_DB]
    except Exception:
        pass
    return []


def save_watchlist(labels: list[str]) -> None:
    """Persist asset labels to CSV. Failure is non-blocking."""
    try:
        WATCHLIST_DIR.mkdir(exist_ok=True)
        with WATCHLIST_FILE.open("w", encoding="utf-8") as f:
            for lbl in labels:
                f.write(lbl + "\n")
    except Exception as e:
        st.toast(f"⚠️ Watchlist save failed: {e}", icon="⚠️")

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE INITIALISATION
# ─────────────────────────────────────────────────────────────────────────────
if "selected_assets" not in st.session_state:
    # Restore watchlist from disk on first render of this session
    st.session_state.selected_assets: list[str] = load_watchlist()
if "selectbox_key" not in st.session_state:
    st.session_state.selectbox_key = 0                 # used to reset the selectbox

# ─────────────────────────────────────────────────────────────────────────────
# DATA FETCHING  (cached)
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data(ttl=3600, show_spinner=False)
def fetch_history(ticker: str) -> pd.DataFrame | None:
    """
    Download 10 years of daily OHLCV data from Yahoo Finance.
    Returns a DataFrame indexed by Date (tz-naive) with columns:
      Open, High, Low, Close, Volume.
    Returns None if data is unavailable or insufficient.

    Defensive normalisations applied (essential for Streamlit Cloud where
    yfinance / pandas versions may differ from local):
      - flatten MultiIndex columns
      - strip timezone from index (prevents concat misalignment across exchanges)
      - force numeric dtype on OHLCV (prevents object-dtype edge cases)
      - drop rows with NaN Close
    """
    end   = date.today()
    start = end - timedelta(days=365 * 10 + 3)          # +3 days buffer for weekends
    try:
        df = yf.download(
            ticker,
            start=start.strftime("%Y-%m-%d"),
            end=end.strftime("%Y-%m-%d"),
            auto_adjust=True,
            progress=False,
        )
        if df is None or df.empty or len(df) < 30:
            return None

        # Flatten multi-level columns (yfinance ≥ 0.2.x returns these even for one ticker)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Convert index to tz-naive datetime — critical for cross-exchange alignment
        df.index = pd.to_datetime(df.index)
        if df.index.tz is not None:
            df.index = df.index.tz_localize(None)

        # Force numeric on OHLCV (some yfinance versions return object dtype)
        for col in ["Open", "High", "Low", "Close", "Volume"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Drop rows with missing Close (essential for downstream calcs)
        df = df.dropna(subset=["Close"])
        if len(df) < 30:
            return None

        return df[["Open", "High", "Low", "Close", "Volume"]]
    except Exception:
        return None


def compute_annual_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    From a daily OHLCV DataFrame, compute per-year summary statistics:
      Year | Open | Close | Δ Abs | Δ % | Cumul % | High | Low
    """
    df = df.copy()
    df["Year"] = df.index.year

    rows = []
    first_price = df["Close"].iloc[0]

    for year, grp in df.groupby("Year"):
        open_price  = grp["Open"].iloc[0]
        close_price = grp["Close"].iloc[-1]
        high        = grp["High"].max()
        low         = grp["Low"].min()
        delta_abs   = close_price - open_price
        delta_pct   = (delta_abs / open_price) * 100 if open_price != 0 else np.nan
        cumul_pct   = ((close_price - first_price) / first_price) * 100 if first_price != 0 else np.nan
        rows.append({
            "Year":     int(year),
            "Open":     round(open_price, 4),
            "Close":    round(close_price, 4),
            "High":     round(high, 4),
            "Low":      round(low, 4),
            "Δ Abs":    round(delta_abs, 4),
            "Δ % (ann)": round(delta_pct, 2),
            "Cumul %":   round(cumul_pct, 2),
        })

    return pd.DataFrame(rows).set_index("Year")


def compute_summary_kpis(df: pd.DataFrame, label: str) -> dict:
    """
    Global KPIs over the full 10-year window:
      - Total Return %
      - CAGR %
      - Max Drawdown %
      - Annualised Volatility %
    """
    close = df["Close"].dropna()
    if close.empty or len(close) < 2:
        return {}

    p0        = float(close.iloc[0])
    p_end     = float(close.iloc[-1])
    years     = (close.index[-1] - close.index[0]).days / 365.25

    total_ret = ((p_end - p0) / p0) * 100
    cagr      = ((p_end / p0) ** (1 / years) - 1) * 100 if years > 0 else np.nan

    daily_ret  = close.pct_change().dropna()
    vol_ann    = float(daily_ret.std() * np.sqrt(252) * 100)

    roll_max   = close.cummax()
    drawdown   = (close - roll_max) / roll_max
    max_dd     = float(drawdown.min() * 100)

    return {
        "label":      label,
        "start":      round(p0, 4),
        "end":        round(p_end, 4),
        "total_ret":  round(total_ret, 2),
        "cagr":       round(cagr, 2),
        "vol":        round(vol_ann, 2),
        "max_dd":     round(max_dd, 2),
        "years":      round(years, 1),
    }


def compute_daily_returns_stats(df: pd.DataFrame) -> dict:
    """Mean, stdev, min, max of daily % returns over the window."""
    r = df["Close"].pct_change().dropna() * 100
    if r.empty:
        return {"mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0, "n": 0}
    return {
        "mean": float(r.mean()),
        "std":  float(r.std()),
        "min":  float(r.min()),
        "max":  float(r.max()),
        "n":    int(len(r)),
    }


def build_claude_export(
    data_map: dict[str, pd.DataFrame],
    kpis_list: list[dict],
    start_d: date,
    end_d: date,
) -> str:
    """
    Build a markdown block that matches the FinDash skill's expected input.
    Includes pre-computed KPIs + per-asset Year-by-Year tables + Daily Returns stats.
    The user copies this once and pastes into Claude — the skill formats it
    without any web search (optimal token mode).
    """
    lines: list[str] = []
    asset_names = ", ".join(lbl.split("(")[0].strip() for lbl in data_map.keys())
    years = (end_d - start_d).days / 365.25

    lines.append(f"# FinDash Export — {asset_names}")
    lines.append(
        f"*Window: {start_d.isoformat()} → {end_d.isoformat()} "
        f"({years:.1f} yrs) · Data via Yahoo Finance / yfinance*"
    )
    lines.append("")

    # ── Global Summary ───────────────────────────────────────────────────────
    lines.append("## 🏁 Global Summary (10 Years)")
    lines.append("")
    lines.append(
        "| Asset | Start Price | End Price | Total Return % | CAGR % | "
        "Ann. Volatility % | Max Drawdown % | Data (yrs) |"
    )
    lines.append("|---|---|---|---|---|---|---|---|")
    for k in kpis_list:
        lines.append(
            f"| {k['label']} "
            f"| {k['start']:,.4f} "
            f"| {k['end']:,.4f} "
            f"| {k['total_ret']:+.2f}% "
            f"| {k['cagr']:+.2f}% "
            f"| {k['vol']:.2f}% "
            f"| {k['max_dd']:.2f}% "
            f"| {k['years']:.1f} |"
        )
    lines.append("")

    # ── Year-by-Year per asset ───────────────────────────────────────────────
    for label, df in data_map.items():
        annual = compute_annual_metrics(df)
        lines.append(f"## 📅 Year-by-Year — {label}")
        lines.append("")
        lines.append(
            "| Year | Open | Close | High | Low | Δ Abs | Δ % (ann) | Cumul % |"
        )
        lines.append("|---|---|---|---|---|---|---|---|")
        for year, row in annual.iterrows():
            lines.append(
                f"| {year} "
                f"| {row['Open']:,.4f} "
                f"| {row['Close']:,.4f} "
                f"| {row['High']:,.4f} "
                f"| {row['Low']:,.4f} "
                f"| {row['Δ Abs']:+,.4f} "
                f"| {row['Δ % (ann)']:+.2f}% "
                f"| {row['Cumul %']:+.2f}% |"
            )
        lines.append("")

    # ── Daily Returns Stats ──────────────────────────────────────────────────
    lines.append("## 📊 Daily Returns Distribution")
    lines.append("")
    for label, df in data_map.items():
        s = compute_daily_returns_stats(df)
        lines.append(
            f"- **{label}** — μ={s['mean']:.3f}%, σ={s['std']:.2f}%, "
            f"min={s['min']:.2f}%, max={s['max']:.2f}% (n={s['n']})"
        )
    lines.append("")
    lines.append("---")
    lines.append(
        "*Generated from FinDash Streamlit platform. Paste into Claude with "
        "the `findash-report` skill enabled to render the full dashboard.*"
    )

    return "\n".join(lines)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 FinDash")
    st.markdown("*10-Year Asset Performance Tracker*")
    st.divider()

    # ── Asset search / add ────────────────────────────────────────────────────
    st.markdown("**Add an asset**")
    chosen_label = st.selectbox(
        "Search by name or ticker",
        options=ASSET_LABELS,
        index=0,
        key=f"asset_selector_{st.session_state.selectbox_key}",
        placeholder="Type to search…",
    )

    if chosen_label and chosen_label not in st.session_state.selected_assets:
        st.session_state.selected_assets.append(chosen_label)
        save_watchlist(st.session_state.selected_assets)   # persist
        st.session_state.selectbox_key += 1   # reset widget to blank
        st.rerun()

    st.divider()

    # ── Current portfolio ─────────────────────────────────────────────────────
    if st.session_state.selected_assets:
        st.markdown("**Portfolio**")
        for idx, label in enumerate(st.session_state.selected_assets):
            col_name, col_btn = st.columns([4, 1])
            col_name.markdown(f"<small>{label}</small>", unsafe_allow_html=True)
            if col_btn.button("❌", key=f"remove_{idx}", help=f"Remove {label}"):
                st.session_state.selected_assets.pop(idx)
                save_watchlist(st.session_state.selected_assets)   # persist
                st.rerun()
        if st.button("🗑️ Clear watchlist", key="clear_all", use_container_width=True):
            st.session_state.selected_assets = []
            save_watchlist([])
            st.rerun()
    else:
        st.info("No assets selected yet.")

    st.divider()
    st.caption(
        "Data via Yahoo Finance · Cached 1 h\n\n"
        "Watchlist auto-saved to `user_data/watchlist.csv`.\n\n"
        "Prices in asset's native currency."
    )

# ─────────────────────────────────────────────────────────────────────────────
# MAIN PANEL
# ─────────────────────────────────────────────────────────────────────────────

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# 📈 Financial Dashboard")
st.markdown(
    f"**10-year window** · {(date.today() - timedelta(days=365*10)).strftime('%d %b %Y')} "
    f"→ {date.today().strftime('%d %b %Y')}"
)
st.divider()

# ── Empty state ───────────────────────────────────────────────────────────────
if not st.session_state.selected_assets:
    st.markdown(
        """
        <div style="text-align:center; padding: 80px 20px; color: #4a5568;">
            <div style="font-size:4rem;">📂</div>
            <h2 style="color:#6e84a3; font-family:'IBM Plex Mono',monospace;">No assets selected</h2>
            <p>Use the <strong>sidebar on the left</strong> to add stocks, indices, ETFs or cryptocurrencies.<br>
            Your selection persists as you explore the dashboard.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────────────────────────────────────
data_map: dict[str, pd.DataFrame] = {}      # label → daily OHLCV
kpis_list: list[dict]              = []

with st.spinner("⏳ Fetching market data…"):
    for label in st.session_state.selected_assets:
        ticker = ASSET_DB[label]
        df = fetch_history(ticker)
        if df is None:
            st.warning(
                f"⚠️  **{label}** — No data available for the requested period. "
                f"The ticker may be delisted, too recent, or temporarily unavailable."
            )
        else:
            data_map[label] = df
            kpis_list.append(compute_summary_kpis(df, label))

if not data_map:
    st.error("No data could be loaded for any selected asset. Please try different tickers.")
    st.stop()

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — GLOBAL KPI SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("## 🏁 Global Summary (10 Years)")

kpi_df = pd.DataFrame(kpis_list).set_index("label")
kpi_df.index.name = "Asset"
kpi_df.columns = ["Start Price", "End Price", "Total Return %", "CAGR %", "Ann. Volatility %", "Max Drawdown %", "Data (yrs)"]

# Display styled dataframe
def color_signed(val):
    if isinstance(val, (int, float)):
        if val > 0:
            return "color: #27ae60; font-weight:600"
        elif val < 0:
            return "color: #e74c3c; font-weight:600"
    return ""

styled = (
    kpi_df.style
    .map(color_signed, subset=["Total Return %", "CAGR %", "Max Drawdown %"])
    .format({
        "Start Price":        "{:,.4f}",
        "End Price":          "{:,.4f}",
        "Total Return %":     "{:+.2f}%",
        "CAGR %":             "{:+.2f}%",
        "Ann. Volatility %":  "{:.2f}%",
        "Max Drawdown %":     "{:.2f}%",
        "Data (yrs)":         "{:.1f}",
    })
    .set_table_styles([
        {"selector": "th", "props": [
            ("background-color", "#151925"),
            ("color", "#8899bb"),
            ("font-family", "'IBM Plex Mono', monospace"),
            ("font-size", "0.78rem"),
            ("text-transform", "uppercase"),
            ("letter-spacing", "0.06em"),
        ]},
        {"selector": "td", "props": [
            ("background-color", "#0d0f14"),
            ("font-family", "'IBM Plex Mono', monospace"),
            ("font-size", "0.88rem"),
        ]},
    ])
)

st.dataframe(styled, use_container_width=True, height=min(60 + 36 * len(kpi_df), 420))

# ── Quick metric row (for first asset only as illustration) ──────────────────
if kpis_list:
    top = kpis_list[0]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Return",    f"{top['total_ret']:+.2f}%")
    c2.metric("CAGR",            f"{top['cagr']:+.2f}%")
    c3.metric("Ann. Volatility", f"{top['vol']:.2f}%")
    c4.metric("Max Drawdown",    f"{top['max_dd']:.2f}%",  delta_color="inverse")

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — NORMALISED PERFORMANCE CHART (Base 100)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("## 📉 Normalised Performance — Base 100")
st.caption("All assets rebased to 100 on day 1 of the window, enabling direct visual comparison.")

normed_frames = []
for label, df in data_map.items():
    close = df["Close"].dropna()
    if close.empty or close.iloc[0] == 0:
        continue
    normed = (close / close.iloc[0]) * 100
    normed.name = label
    normed_frames.append(normed)

if normed_frames:
    chart_df = pd.concat(normed_frames, axis=1).ffill()
    # Strip tz again defensively (concat can re-introduce it from individual series)
    chart_df.index = pd.to_datetime(chart_df.index)
    if chart_df.index.tz is not None:
        chart_df.index = chart_df.index.tz_localize(None)
    # Resample to weekly to keep the chart readable
    chart_df_weekly = chart_df.resample("W").last().dropna(how="all")

    if chart_df_weekly.empty or chart_df_weekly.isna().all().all():
        st.warning("⚠️ Chart data is empty after processing. Open the debug panel below.")
        with st.expander("🐛 Debug — raw chart data shape"):
            st.write(f"chart_df shape: {chart_df.shape}")
            st.write(f"chart_df_weekly shape: {chart_df_weekly.shape}")
            st.write("chart_df head:")
            st.write(chart_df.head())
            st.write("chart_df_weekly head:")
            st.write(chart_df_weekly.head())
    else:
        st.line_chart(chart_df_weekly, use_container_width=True, height=380)
else:
    st.warning("⚠️ No assets with valid data for normalisation.")

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — PER-ASSET ANNUAL BREAKDOWN  (Tabs)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("## 📅 Year-by-Year Breakdown")
st.caption("Annual open, close, gain/loss, % performance and cumulative return since start.")

tabs = st.tabs([lbl.split("(")[0].strip() for lbl in data_map.keys()])

for tab, (label, df) in zip(tabs, data_map.items()):
    with tab:
        annual = compute_annual_metrics(df)

        def annual_color(val, col_name):
            """Apply green/red to signed columns."""
            if col_name in ["Δ Abs", "Δ % (ann)", "Cumul %"]:
                if isinstance(val, (int, float)):
                    return "color:#27ae60;font-weight:600" if val >= 0 else "color:#e74c3c;font-weight:600"
            return ""

        styled_ann = (
            annual.style
            .apply(
                lambda col: [annual_color(v, col.name) for v in col],
                axis=0,
            )
            .format({
                "Open":       "{:,.4f}",
                "Close":      "{:,.4f}",
                "High":       "{:,.4f}",
                "Low":        "{:,.4f}",
                "Δ Abs":      "{:+,.4f}",
                "Δ % (ann)":  "{:+.2f}%",
                "Cumul %":    "{:+.2f}%",
            })
            .set_table_styles([
                {"selector": "th", "props": [
                    ("background-color", "#151925"),
                    ("color", "#8899bb"),
                    ("font-family", "'IBM Plex Mono', monospace"),
                    ("font-size", "0.76rem"),
                    ("text-transform", "uppercase"),
                ]},
                {"selector": "td", "props": [
                    ("background-color", "#0d0f14"),
                    ("font-family", "'IBM Plex Mono', monospace"),
                    ("font-size", "0.86rem"),
                ]},
            ])
        )

        st.dataframe(styled_ann, use_container_width=True, height=min(60 + 36 * len(annual), 480))

        # ── Sparkline for this asset ─────────────────────────────────────────
        st.caption(f"📈 Closing price history — {label}")
        close_series = df["Close"].dropna()
        if not close_series.empty:
            # Strip tz before resample (defensive)
            close_series.index = pd.to_datetime(close_series.index)
            if close_series.index.tz is not None:
                close_series.index = close_series.index.tz_localize(None)
            weekly = close_series.resample("W").last().dropna().to_frame()
            if not weekly.empty:
                st.line_chart(weekly, use_container_width=True, height=200)
            else:
                st.caption("_(no data to plot)_")
        else:
            st.caption("_(no data to plot)_")

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — RETURNS DISTRIBUTION  (histogram via native chart)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("## 📊 Daily Returns Distribution")
st.caption("Histogram of daily percentage returns (binned to 50 buckets). Fat tails = higher volatility.")

ret_frames = []
for label, df in data_map.items():
    daily_ret = df["Close"].pct_change().dropna() * 100
    daily_ret.name = label
    ret_frames.append(daily_ret)

if ret_frames:
    ret_df = pd.concat(ret_frames, axis=1)

    # Build histogram manually (bin counts) for each asset
    bins = np.linspace(ret_df.min().min(), ret_df.max().max(), 51)
    hist_data = {}
    bin_labels = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]
    for col in ret_df.columns:
        counts, _ = np.histogram(ret_df[col].dropna(), bins=bins)
        hist_data[col] = counts

    hist_df = pd.DataFrame(hist_data, index=[round(b, 2) for b in bin_labels])
    hist_df.index.name = "Daily Return (%)"
    st.bar_chart(hist_df, use_container_width=True, height=300)

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — EXPORT FOR CLAUDE  (paste-friendly markdown)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("## 📋 Export for Claude")
st.caption(
    "Copy the block below, paste into Claude with the **`findash-report`** skill "
    "enabled. Claude will render the full FinDash dashboard report in seconds — "
    "no web search needed (optimal token mode)."
)

# Window dates (must mirror fetch_history exactly)
_end_d   = date.today()
_start_d = _end_d - timedelta(days=365 * 10 + 3)

export_md = build_claude_export(data_map, kpis_list, _start_d, _end_d)

# Native copy-button via st.code
st.code(export_md, language="markdown")

# Download as .md file (alternative for offline use)
col_a, col_b = st.columns([1, 4])
with col_a:
    st.download_button(
        label="⬇️ Download .md",
        data=export_md,
        file_name=f"findash_export_{_end_d.isoformat()}.md",
        mime="text/markdown",
        use_container_width=True,
    )
with col_b:
    st.caption(
        f"💾 {len(export_md):,} characters · "
        f"{len(data_map)} asset(s) · "
        "watchlist auto-saved to `user_data/watchlist.csv`"
    )

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="text-align:center; padding:20px 0 8px; color:#3a4a5f; font-size:0.75rem;">
        FinDash · Data sourced from <strong>Yahoo Finance</strong> via <em>yfinance</em> ·
        For informational purposes only. Not financial advice.
    </div>
    """,
    unsafe_allow_html=True,
)