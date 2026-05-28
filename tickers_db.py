"""
tickers_db.py — Extended Asset Database for FinDash
====================================================

~1500+ Yahoo Finance tickers grouped by index/market.
Imported by app.py and merged into ASSET_DB.

Format per entry: ("Display Name", "YAHOO_TICKER")
Final dict key: "Display Name (YAHOO_TICKER)"  (matches app.py convention)

⚠️ Some tickers may be outdated (delistings, ticker changes after the
generation date). The Streamlit app handles missing data gracefully
(displays a warning). You can edit this file freely to add/fix entries.

Yahoo Finance ticker suffix reference:
  .PA  Paris (Euronext)        .AS  Amsterdam       .BR  Brussels
  .LS  Lisbon                  .DE  Frankfurt (XETRA)
  .L   London (LSE)            .MI  Milan           .MC  Madrid (BME)
  .SW  Swiss (SIX)             .OL  Oslo            .ST  Stockholm
  .HE  Helsinki                .CO  Copenhagen      .IR  Ireland
  .VI  Vienna                  .WA  Warsaw          .T   Tokyo
  .HK  Hong Kong               .SS  Shanghai        .SZ  Shenzhen
  .KS  Seoul                   .TW  Taiwan          .AX  Australia (ASX)
  .NS  India (NSE)             .SA  São Paulo       .MX  Mexico (BMV)
  .JO  Johannesburg            .TA  Tel Aviv
  Cryptos: format  TICKER-USD  (e.g. BTC-USD)
  Indices: prefix  ^           (e.g. ^GSPC)
"""

# =============================================================================
# UNITED STATES — S&P 500 (alphabetical)
# =============================================================================
SP500 = [
    ("Apple Inc.", "AAPL"), ("AbbVie Inc.", "ABBV"), ("Abbott Laboratories", "ABT"),
    ("Accenture plc", "ACN"), ("Adobe Inc.", "ADBE"), ("Analog Devices", "ADI"),
    ("Archer-Daniels-Midland", "ADM"), ("Automatic Data Processing", "ADP"),
    ("Autodesk Inc.", "ADSK"), ("Ameren Corp.", "AEE"), ("American Electric Power", "AEP"),
    ("AES Corp.", "AES"), ("Aflac Inc.", "AFL"), ("AIG", "AIG"),
    ("Assurant Inc.", "AIZ"), ("Arthur J. Gallagher", "AJG"), ("Akamai Technologies", "AKAM"),
    ("Albemarle Corp.", "ALB"), ("Align Technology", "ALGN"), ("Allstate Corp.", "ALL"),
    ("Allegion plc", "ALLE"), ("Applied Materials", "AMAT"), ("Amcor plc", "AMCR"),
    ("Advanced Micro Devices", "AMD"), ("AMETEK Inc.", "AME"), ("Amgen Inc.", "AMGN"),
    ("Ameriprise Financial", "AMP"), ("American Tower", "AMT"), ("Amazon.com", "AMZN"),
    ("Arista Networks", "ANET"), ("Ansys Inc.", "ANSS"), ("Aon plc", "AON"),
    ("A.O. Smith", "AOS"), ("APA Corp.", "APA"), ("Air Products", "APD"),
    ("Amphenol Corp.", "APH"), ("Apollo Global Mgmt", "APO"), ("Aptiv plc", "APTV"),
    ("Alexandria Real Estate", "ARE"), ("Atmos Energy", "ATO"), ("AvalonBay Communities", "AVB"),
    ("Broadcom Inc.", "AVGO"), ("Avery Dennison", "AVY"), ("American Water Works", "AWK"),
    ("Axon Enterprise", "AXON"), ("American Express", "AXP"), ("AutoZone Inc.", "AZO"),
    ("Boeing Co.", "BA"), ("Bank of America", "BAC"), ("Ball Corp.", "BALL"),
    ("Baxter International", "BAX"), ("Bath & Body Works", "BBWI"), ("Best Buy", "BBY"),
    ("Becton Dickinson", "BDX"), ("Franklin Resources", "BEN"), ("Brown-Forman B", "BF-B"),
    ("Biogen Inc.", "BIIB"), ("Bio-Rad Laboratories", "BIO"), ("Bank of New York Mellon", "BK"),
    ("Booking Holdings", "BKNG"), ("Baker Hughes", "BKR"), ("Builders FirstSource", "BLDR"),
    ("BlackRock Inc.", "BLK"), ("Bristol-Myers Squibb", "BMY"), ("Broadridge Financial", "BR"),
    ("Berkshire Hathaway B", "BRK-B"), ("Brown & Brown", "BRO"), ("Boston Scientific", "BSX"),
    ("BorgWarner Inc.", "BWA"), ("Blackstone Inc.", "BX"), ("Boston Properties", "BXP"),
    ("Citigroup Inc.", "C"), ("Conagra Brands", "CAG"), ("Cardinal Health", "CAH"),
    ("Carrier Global", "CARR"), ("Caterpillar Inc.", "CAT"), ("Chubb Limited", "CB"),
    ("CBOE Global Markets", "CBOE"), ("CBRE Group", "CBRE"), ("Crown Castle", "CCI"),
    ("Carnival Corp.", "CCL"), ("Cadence Design Systems", "CDNS"), ("CDW Corp.", "CDW"),
    ("Celanese Corp.", "CE"), ("Constellation Energy", "CEG"), ("CF Industries", "CF"),
    ("Citizens Financial", "CFG"), ("Church & Dwight", "CHD"), ("C.H. Robinson", "CHRW"),
    ("Charter Communications", "CHTR"), ("Cigna Group", "CI"), ("Cincinnati Financial", "CINF"),
    ("Colgate-Palmolive", "CL"), ("Clorox Co.", "CLX"), ("Comerica Inc.", "CMA"),
    ("Comcast Corp.", "CMCSA"), ("CME Group", "CME"), ("Chipotle Mexican Grill", "CMG"),
    ("Cummins Inc.", "CMI"), ("CMS Energy", "CMS"), ("Centene Corp.", "CNC"),
    ("CenterPoint Energy", "CNP"), ("Capital One Financial", "COF"), ("Cooper Companies", "COO"),
    ("ConocoPhillips", "COP"), ("Cencora Inc.", "COR"), ("Costco Wholesale", "COST"),
    ("Campbell Soup", "CPB"), ("Copart Inc.", "CPRT"), ("Camden Property Trust", "CPT"),
    ("Charles River Laboratories", "CRL"), ("Salesforce Inc.", "CRM"), ("CrowdStrike Holdings", "CRWD"),
    ("Cisco Systems", "CSCO"), ("CoStar Group", "CSGP"), ("CSX Corp.", "CSX"),
    ("Cintas Corp.", "CTAS"), ("Catalent Inc.", "CTLT"), ("Coterra Energy", "CTRA"),
    ("Cognizant Technology", "CTSH"), ("Corteva Inc.", "CTVA"), ("CVS Health", "CVS"),
    ("Chevron Corp.", "CVX"), ("Caesars Entertainment", "CZR"),
    ("Dominion Energy", "D"), ("Delta Air Lines", "DAL"), ("DoorDash Inc.", "DASH"),
    ("Dayforce Inc.", "DAY"), ("DuPont de Nemours", "DD"), ("Deere & Co.", "DE"),
    ("Deckers Outdoor", "DECK"), ("Discover Financial", "DFS"), ("Dollar General", "DG"),
    ("Quest Diagnostics", "DGX"), ("D.R. Horton", "DHI"), ("Danaher Corp.", "DHR"),
    ("Walt Disney Co.", "DIS"), ("Digital Realty Trust", "DLR"), ("Dollar Tree", "DLTR"),
    ("Healthpeak Properties", "DOC"), ("Dover Corp.", "DOV"), ("Dow Inc.", "DOW"),
    ("Domino's Pizza", "DPZ"), ("Darden Restaurants", "DRI"), ("DTE Energy", "DTE"),
    ("Duke Energy", "DUK"), ("DaVita Inc.", "DVA"), ("Devon Energy", "DVN"),
    ("DexCom Inc.", "DXCM"),
    ("Electronic Arts", "EA"), ("eBay Inc.", "EBAY"), ("Ecolab Inc.", "ECL"),
    ("Consolidated Edison", "ED"), ("Equifax Inc.", "EFX"), ("Everest Group", "EG"),
    ("Edison International", "EIX"), ("Estee Lauder", "EL"), ("Elevance Health", "ELV"),
    ("Eastman Chemical", "EMN"), ("Emerson Electric", "EMR"), ("Enphase Energy", "ENPH"),
    ("EOG Resources", "EOG"), ("EPAM Systems", "EPAM"), ("Equinix Inc.", "EQIX"),
    ("Equity Residential", "EQR"), ("EQT Corp.", "EQT"), ("Eversource Energy", "ES"),
    ("Essex Property Trust", "ESS"), ("Eaton Corp.", "ETN"), ("Entergy Corp.", "ETR"),
    ("Etsy Inc.", "ETSY"), ("Evergy Inc.", "EVRG"), ("Edwards Lifesciences", "EW"),
    ("Exelon Corp.", "EXC"), ("Expeditors Intl", "EXPD"), ("Expedia Group", "EXPE"),
    ("Extra Space Storage", "EXR"),
    ("Ford Motor Co.", "F"), ("Diamondback Energy", "FANG"), ("Fastenal Co.", "FAST"),
    ("Freeport-McMoRan", "FCX"), ("FactSet Research", "FDS"), ("FedEx Corp.", "FDX"),
    ("FirstEnergy Corp.", "FE"), ("F5 Inc.", "FFIV"), ("Fiserv Inc.", "FI"),
    ("Fair Isaac Corp.", "FICO"), ("Fidelity National Info", "FIS"), ("Fifth Third Bancorp", "FITB"),
    ("FMC Corp.", "FMC"), ("Fox Corp. B", "FOX"), ("Fox Corp. A", "FOXA"),
    ("Federal Realty Trust", "FRT"), ("First Solar", "FSLR"), ("Fortinet Inc.", "FTNT"),
    ("Fortive Corp.", "FTV"),
    ("General Dynamics", "GD"), ("General Electric", "GE"), ("GE HealthCare", "GEHC"),
    ("Gen Digital", "GEN"), ("GE Vernova", "GEV"), ("Gilead Sciences", "GILD"),
    ("General Mills", "GIS"), ("Globe Life", "GL"), ("Corning Inc.", "GLW"),
    ("General Motors", "GM"), ("Generac Holdings", "GNRC"), ("Alphabet Inc. C", "GOOG"),
    ("Alphabet Inc. A", "GOOGL"), ("Genuine Parts Co.", "GPC"), ("Global Payments", "GPN"),
    ("Garmin Ltd.", "GRMN"), ("Goldman Sachs", "GS"), ("W.W. Grainger", "GWW"),
    ("Halliburton Co.", "HAL"), ("Hasbro Inc.", "HAS"), ("Huntington Bancshares", "HBAN"),
    ("HCA Healthcare", "HCA"), ("Home Depot", "HD"), ("Hess Corp.", "HES"),
    ("Hartford Financial", "HIG"), ("Huntington Ingalls", "HII"), ("Hilton Worldwide", "HLT"),
    ("Hologic Inc.", "HOLX"), ("Honeywell Intl", "HON"), ("Hewlett Packard Enterprise", "HPE"),
    ("HP Inc.", "HPQ"), ("Hormel Foods", "HRL"), ("Henry Schein", "HSIC"),
    ("Host Hotels & Resorts", "HST"), ("Hershey Co.", "HSY"), ("Hubbell Inc.", "HUBB"),
    ("Humana Inc.", "HUM"), ("Howmet Aerospace", "HWM"),
    ("IBM Corp.", "IBM"), ("Intercontinental Exchange", "ICE"), ("IDEXX Laboratories", "IDXX"),
    ("IDEX Corp.", "IEX"), ("Intl Flavors & Fragrances", "IFF"), ("Incyte Corp.", "INCY"),
    ("Intel Corp.", "INTC"), ("Intuit Inc.", "INTU"), ("Invitation Homes", "INVH"),
    ("Intl Paper", "IP"), ("Interpublic Group", "IPG"), ("IQVIA Holdings", "IQV"),
    ("Ingersoll Rand", "IR"), ("Iron Mountain", "IRM"), ("Intuitive Surgical", "ISRG"),
    ("Gartner Inc.", "IT"), ("Illinois Tool Works", "ITW"), ("Invesco Ltd.", "IVZ"),
    ("Jacobs Solutions", "J"), ("J.B. Hunt Transport", "JBHT"), ("Jabil Inc.", "JBL"),
    ("Johnson Controls", "JCI"), ("Jack Henry & Associates", "JKHY"), ("Johnson & Johnson", "JNJ"),
    ("Juniper Networks", "JNPR"), ("JPMorgan Chase", "JPM"),
    ("Kellanova", "K"), ("Keurig Dr Pepper", "KDP"), ("KeyCorp", "KEY"),
    ("Keysight Technologies", "KEYS"), ("Kraft Heinz", "KHC"), ("Kimco Realty", "KIM"),
    ("KKR & Co.", "KKR"), ("KLA Corp.", "KLAC"), ("Kimberly-Clark", "KMB"),
    ("Kinder Morgan", "KMI"), ("CarMax Inc.", "KMX"), ("Coca-Cola Co.", "KO"),
    ("Kroger Co.", "KR"), ("Kenvue Inc.", "KVUE"),
    ("Loews Corp.", "L"), ("Leidos Holdings", "LDOS"), ("Lennar Corp.", "LEN"),
    ("LabCorp Holdings", "LH"), ("L3Harris Technologies", "LHX"), ("Linde plc", "LIN"),
    ("LKQ Corp.", "LKQ"), ("Eli Lilly & Co.", "LLY"), ("Lockheed Martin", "LMT"),
    ("Alliant Energy", "LNT"), ("Lowe's Companies", "LOW"), ("Lam Research", "LRCX"),
    ("Lululemon Athletica", "LULU"), ("Southwest Airlines", "LUV"), ("Las Vegas Sands", "LVS"),
    ("Lamb Weston Holdings", "LW"), ("LyondellBasell Industries", "LYB"), ("Live Nation Entertainment", "LYV"),
    ("Mastercard Inc.", "MA"), ("Mid-America Apartments", "MAA"), ("Marriott Intl", "MAR"),
    ("Masco Corp.", "MAS"), ("McDonald's Corp.", "MCD"), ("Microchip Technology", "MCHP"),
    ("McKesson Corp.", "MCK"), ("Moody's Corp.", "MCO"), ("Mondelez Intl", "MDLZ"),
    ("Medtronic plc", "MDT"), ("MetLife Inc.", "MET"), ("Meta Platforms", "META"),
    ("MGM Resorts Intl", "MGM"), ("Mohawk Industries", "MHK"), ("McCormick & Co.", "MKC"),
    ("MarketAxess Holdings", "MKTX"), ("Martin Marietta Materials", "MLM"), ("Marsh & McLennan", "MMC"),
    ("3M Co.", "MMM"), ("Monster Beverage", "MNST"), ("Altria Group", "MO"),
    ("Molina Healthcare", "MOH"), ("Mosaic Co.", "MOS"), ("Marathon Petroleum", "MPC"),
    ("Monolithic Power Systems", "MPWR"), ("Merck & Co.", "MRK"), ("Moderna Inc.", "MRNA"),
    ("Morgan Stanley", "MS"), ("MSCI Inc.", "MSCI"), ("Microsoft Corp.", "MSFT"),
    ("Motorola Solutions", "MSI"), ("M&T Bank", "MTB"), ("Match Group", "MTCH"),
    ("Mettler-Toledo Intl", "MTD"), ("Micron Technology", "MU"),
    ("Norwegian Cruise Line", "NCLH"), ("Nasdaq Inc.", "NDAQ"), ("Nordson Corp.", "NDSN"),
    ("NextEra Energy", "NEE"), ("Newmont Corp.", "NEM"), ("Netflix Inc.", "NFLX"),
    ("NiSource Inc.", "NI"), ("Nike Inc.", "NKE"), ("Northrop Grumman", "NOC"),
    ("ServiceNow Inc.", "NOW"), ("NRG Energy", "NRG"), ("Norfolk Southern", "NSC"),
    ("NetApp Inc.", "NTAP"), ("Northern Trust", "NTRS"), ("Nucor Corp.", "NUE"),
    ("NVIDIA Corp.", "NVDA"), ("NVR Inc.", "NVR"), ("News Corp. B", "NWS"),
    ("News Corp. A", "NWSA"), ("NXP Semiconductors", "NXPI"),
    ("Realty Income", "O"), ("Old Dominion Freight Line", "ODFL"), ("ONEOK Inc.", "OKE"),
    ("Omnicom Group", "OMC"), ("ON Semiconductor", "ON"), ("Oracle Corp.", "ORCL"),
    ("O'Reilly Automotive", "ORLY"), ("Otis Worldwide", "OTIS"), ("Occidental Petroleum", "OXY"),
    ("Palo Alto Networks", "PANW"), ("Paramount Global B", "PARA"), ("Paycom Software", "PAYC"),
    ("Paychex Inc.", "PAYX"), ("PACCAR Inc.", "PCAR"), ("PG&E Corp.", "PCG"),
    ("Public Service Enterprise", "PEG"), ("PepsiCo Inc.", "PEP"), ("Pfizer Inc.", "PFE"),
    ("Principal Financial", "PFG"), ("Procter & Gamble", "PG"), ("Progressive Corp.", "PGR"),
    ("Parker-Hannifin", "PH"), ("PulteGroup Inc.", "PHM"), ("Packaging Corp.", "PKG"),
    ("Prologis Inc.", "PLD"), ("Palantir Technologies", "PLTR"), ("Philip Morris Intl", "PM"),
    ("PNC Financial Services", "PNC"), ("Pentair plc", "PNR"), ("Pinnacle West Capital", "PNW"),
    ("Insulet Corp.", "PODD"), ("Pool Corp.", "POOL"), ("PPG Industries", "PPG"),
    ("PPL Corp.", "PPL"), ("Prudential Financial", "PRU"), ("Public Storage", "PSA"),
    ("Phillips 66", "PSX"), ("PTC Inc.", "PTC"), ("Quanta Services", "PWR"),
    ("PayPal Holdings", "PYPL"),
    ("Qualcomm Inc.", "QCOM"), ("Qorvo Inc.", "QRVO"),
    ("Royal Caribbean Cruises", "RCL"), ("Regency Centers", "REG"), ("Regeneron Pharmaceuticals", "REGN"),
    ("Regions Financial", "RF"), ("Raymond James Financial", "RJF"), ("Ralph Lauren", "RL"),
    ("ResMed Inc.", "RMD"), ("Rockwell Automation", "ROK"), ("Rollins Inc.", "ROL"),
    ("Roper Technologies", "ROP"), ("Ross Stores", "ROST"), ("Republic Services", "RSG"),
    ("RTX Corp.", "RTX"), ("Revvity Inc.", "RVTY"),
    ("SBA Communications", "SBAC"), ("Starbucks Corp.", "SBUX"), ("Charles Schwab", "SCHW"),
    ("Sherwin-Williams Co.", "SHW"), ("J.M. Smucker Co.", "SJM"), ("Schlumberger NV", "SLB"),
    ("Super Micro Computer", "SMCI"), ("Snap-on Inc.", "SNA"), ("Synopsys Inc.", "SNPS"),
    ("Southern Co.", "SO"), ("Solventum Corp.", "SOLV"), ("Simon Property Group", "SPG"),
    ("S&P Global Inc.", "SPGI"), ("Sempra Energy", "SRE"), ("Steris plc", "STE"),
    ("Steel Dynamics", "STLD"), ("State Street Corp.", "STT"), ("Seagate Technology", "STX"),
    ("Constellation Brands", "STZ"), ("Smurfit Westrock", "SW"), ("Stanley Black & Decker", "SWK"),
    ("Skyworks Solutions", "SWKS"), ("Synchrony Financial", "SYF"), ("Stryker Corp.", "SYK"),
    ("Sysco Corp.", "SYY"),
    ("AT&T Inc.", "T"), ("Molson Coors Beverage", "TAP"), ("TransDigm Group", "TDG"),
    ("Teledyne Technologies", "TDY"), ("Bio-Techne Corp.", "TECH"), ("TE Connectivity", "TEL"),
    ("Teradyne Inc.", "TER"), ("Truist Financial", "TFC"), ("Teleflex Inc.", "TFX"),
    ("Target Corp.", "TGT"), ("TJX Companies", "TJX"), ("Thermo Fisher Scientific", "TMO"),
    ("T-Mobile US", "TMUS"), ("Texas Pacific Land", "TPL"), ("Tapestry Inc.", "TPR"),
    ("Targa Resources", "TRGP"), ("Trimble Inc.", "TRMB"), ("T. Rowe Price Group", "TROW"),
    ("Travelers Companies", "TRV"), ("Tractor Supply Co.", "TSCO"), ("Tesla Inc.", "TSLA"),
    ("Tyson Foods", "TSN"), ("Trane Technologies", "TT"), ("Take-Two Interactive", "TTWO"),
    ("Texas Instruments", "TXN"), ("Textron Inc.", "TXT"), ("Tyler Technologies", "TYL"),
    ("United Airlines Holdings", "UAL"), ("Uber Technologies", "UBER"), ("UDR Inc.", "UDR"),
    ("Universal Health Services", "UHS"), ("Ulta Beauty", "ULTA"), ("UnitedHealth Group", "UNH"),
    ("Union Pacific Corp.", "UNP"), ("United Parcel Service", "UPS"), ("United Rentals", "URI"),
    ("U.S. Bancorp", "USB"),
    ("Visa Inc.", "V"), ("VICI Properties", "VICI"), ("Valero Energy", "VLO"),
    ("Veralto Corp.", "VLTO"), ("Vulcan Materials", "VMC"), ("Verisk Analytics", "VRSK"),
    ("VeriSign Inc.", "VRSN"), ("Vertex Pharmaceuticals", "VRTX"), ("Vistra Corp.", "VST"),
    ("Ventas Inc.", "VTR"), ("Viatris Inc.", "VTRS"), ("Verizon Communications", "VZ"),
    ("Wabtec Corp.", "WAB"), ("Waters Corp.", "WAT"), ("Walgreens Boots Alliance", "WBA"),
    ("Warner Bros. Discovery", "WBD"), ("Western Digital", "WDC"), ("WEC Energy Group", "WEC"),
    ("Welltower Inc.", "WELL"), ("Wells Fargo", "WFC"), ("Waste Management", "WM"),
    ("Williams Companies", "WMB"), ("Walmart Inc.", "WMT"), ("W.R. Berkley", "WRB"),
    ("West Pharmaceutical Services", "WST"), ("Willis Towers Watson", "WTW"),
    ("Weyerhaeuser Co.", "WY"), ("Wynn Resorts", "WYNN"),
    ("Xcel Energy", "XEL"), ("Exxon Mobil", "XOM"), ("Xylem Inc.", "XYL"),
    ("Yum! Brands", "YUM"),
    ("Zimmer Biomet", "ZBH"), ("Zebra Technologies", "ZBRA"), ("Zoetis Inc.", "ZTS"),
]

# =============================================================================
# UNITED STATES — NASDAQ-100 supplements (not in S&P 500)
# =============================================================================
NASDAQ100_EXTRA = [
    ("MercadoLibre Inc.", "MELI"), ("PDD Holdings", "PDD"), ("Atlassian Corp.", "TEAM"),
    ("Workday Inc.", "WDAY"), ("Zscaler Inc.", "ZS"), ("DataDog Inc.", "DDOG"),
    ("Marvell Technology", "MRVL"), ("Cognizant Technology", "CTSH"),
    ("Lucid Group", "LCID"), ("Rivian Automotive", "RIVN"), ("Robinhood Markets", "HOOD"),
    ("Coinbase Global", "COIN"), ("Roblox Corp.", "RBLX"), ("Snowflake Inc.", "SNOW"),
    ("Cloudflare Inc.", "NET"), ("Twilio Inc.", "TWLO"), ("Okta Inc.", "OKTA"),
    ("MongoDB Inc.", "MDB"), ("Pinterest Inc.", "PINS"), ("Snap Inc.", "SNAP"),
    ("DraftKings Inc.", "DKNG"), ("Unity Software", "U"), ("Block Inc.", "SQ"),
    ("Shopify Inc.", "SHOP"), ("Spotify Technology", "SPOT"), ("Sea Limited", "SE"),
    ("Affirm Holdings", "AFRM"), ("UiPath Inc.", "PATH"), ("Toast Inc.", "TOST"),
    ("Reddit Inc.", "RDDT"), ("Astera Labs", "ALAB"), ("CAVA Group", "CAVA"),
]

# =============================================================================
# FRANCE — CAC 40
# =============================================================================
CAC40 = [
    ("Accor SA", "AC.PA"), ("Air Liquide", "AI.PA"), ("Airbus SE", "AIR.PA"),
    ("Arkema SA", "AKE.PA"), ("Axa SA", "CS.PA"), ("BNP Paribas", "BNP.PA"),
    ("Bouygues SA", "EN.PA"), ("Bureau Veritas", "BVI.PA"), ("Capgemini SE", "CAP.PA"),
    ("Carrefour SA", "CA.PA"), ("Crédit Agricole", "ACA.PA"), ("Dassault Systèmes", "DSY.PA"),
    ("Danone SA", "BN.PA"), ("Edenred", "EDEN.PA"), ("Engie SA", "ENGI.PA"),
    ("EssilorLuxottica", "EL.PA"), ("Eurofins Scientific", "ERF.PA"), ("Hermès Intl", "RMS.PA"),
    ("Kering SA", "KER.PA"), ("L'Oréal SA", "OR.PA"), ("Legrand SA", "LR.PA"),
    ("LVMH Moët Hennessy", "MC.PA"), ("Michelin", "ML.PA"), ("Orange SA", "ORA.PA"),
    ("Pernod Ricard", "RI.PA"), ("Publicis Groupe", "PUB.PA"), ("Renault SA", "RNO.PA"),
    ("Safran SA", "SAF.PA"), ("Saint-Gobain", "SGO.PA"), ("Sanofi SA", "SAN.PA"),
    ("Schneider Electric", "SU.PA"), ("Société Générale", "GLE.PA"), ("Stellantis NV", "STLAM.MI"),
    ("STMicroelectronics", "STMPA.PA"), ("Teleperformance", "TEP.PA"), ("Thales SA", "HO.PA"),
    ("TotalEnergies SE", "TTE.PA"), ("Unibail-Rodamco-Westfield", "URW.AS"), ("Veolia Environnement", "VIE.PA"),
    ("Vinci SA", "DG.PA"), ("Vivendi SE", "VIV.PA"), ("Worldline SA", "WLN.PA"),
]

# =============================================================================
# FRANCE — SBF 120 supplement (companies beyond CAC 40)
# =============================================================================
SBF120_EXTRA = [
    ("Alstom SA", "ALO.PA"), ("Amundi SA", "AMUN.PA"), ("Aperam SA", "APAM.AS"),
    ("Atos SE", "ATO.PA"), ("BIC Société", "BB.PA"), ("Bolloré SE", "BOL.PA"),
    ("CGG SA", "CGG.PA"), ("Coface SA", "COFA.PA"), ("Covivio SA", "COV.PA"),
    ("Derichebourg SA", "DBG.PA"), ("Eiffage SA", "FGR.PA"), ("Elis SA", "ELIS.PA"),
    ("Eramet SA", "ERA.PA"), ("Euronext NV", "ENX.PA"), ("Faurecia (Forvia)", "FRVIA.PA"),
    ("FDJ Française des Jeux", "FDJ.PA"), ("Gecina SA", "GFC.PA"), ("Getlink SE", "GET.PA"),
    ("Icade SA", "ICAD.PA"), ("Imerys SA", "NK.PA"), ("Inwit SA", "INWT.PA"),
    ("Ipsen SA", "IPN.PA"), ("Ipsos SA", "IPS.PA"), ("JCDecaux SE", "DEC.PA"),
    ("Klepierre SA", "LI.PA"), ("Lagardère SA", "MMB.PA"), ("Mercialys SA", "MERY.PA"),
    ("Mersen SA", "MRN.PA"), ("Nexans SA", "NEX.PA"), ("OVH Groupe", "OVH.PA"),
    ("Plastic Omnium", "POM.PA"), ("Quadient SA", "QDT.PA"), ("Remy Cointreau", "RCO.PA"),
    ("Rexel SA", "RXL.PA"), ("Rubis SCA", "RUI.PA"), ("Sartorius Stedim", "DIM.PA"),
    ("Scor SE", "SCR.PA"), ("Soitec SA", "SOI.PA"), ("Sopra Steria Group", "SOP.PA"),
    ("SPIE SA", "SPIE.PA"), ("Tarkett SA", "TKTT.PA"), ("Technip Energies", "TE.PA"),
    ("TF1 Group", "TFI.PA"), ("Trigano SA", "TRI.PA"), ("Ubisoft Entertainment", "UBI.PA"),
    ("Valeo SA", "FR.PA"), ("Vallourec SA", "VK.PA"), ("Verallia SA", "VRLA.PA"),
    ("Wendel SE", "MF.PA"),
]

# =============================================================================
# GERMANY — DAX 40
# =============================================================================
DAX40 = [
    ("Adidas AG", "ADS.DE"), ("Airbus SE", "AIR.DE"), ("Allianz SE", "ALV.DE"),
    ("BASF SE", "BAS.DE"), ("Bayer AG", "BAYN.DE"), ("Beiersdorf AG", "BEI.DE"),
    ("BMW AG", "BMW.DE"), ("Brenntag SE", "BNR.DE"), ("Commerzbank AG", "CBK.DE"),
    ("Continental AG", "CON.DE"), ("Covestro AG", "1COV.DE"), ("Daimler Truck Holding", "DTG.DE"),
    ("Deutsche Bank AG", "DBK.DE"), ("Deutsche Börse AG", "DB1.DE"), ("Deutsche Post (DHL)", "DHL.DE"),
    ("Deutsche Telekom AG", "DTE.DE"), ("E.ON SE", "EOAN.DE"), ("Fresenius SE", "FRE.DE"),
    ("Hannover Rück SE", "HNR1.DE"), ("HeidelbergCement (Heidelberg Materials)", "HEI.DE"),
    ("Henkel AG", "HEN3.DE"), ("Infineon Technologies", "IFX.DE"), ("Mercedes-Benz Group", "MBG.DE"),
    ("Merck KGaA", "MRK.DE"), ("MTU Aero Engines", "MTX.DE"), ("Münchener Rück", "MUV2.DE"),
    ("Porsche AG", "P911.DE"), ("Porsche Holding", "PAH3.DE"), ("Puma SE", "PUM.DE"),
    ("Qiagen NV", "QIA.DE"), ("Rheinmetall AG", "RHM.DE"), ("RWE AG", "RWE.DE"),
    ("SAP SE", "SAP.DE"), ("Sartorius AG", "SRT3.DE"), ("Siemens AG", "SIE.DE"),
    ("Siemens Energy", "ENR.DE"), ("Siemens Healthineers", "SHL.DE"), ("Symrise AG", "SY1.DE"),
    ("Volkswagen AG", "VOW3.DE"), ("Vonovia SE", "VNA.DE"), ("Zalando SE", "ZAL.DE"),
]

# =============================================================================
# GERMANY — MDAX selected (mid-cap)
# =============================================================================
MDAX_SELECTED = [
    ("Aixtron SE", "AIXA.DE"), ("Aurubis AG", "NDA.DE"), ("Bechtle AG", "BC8.DE"),
    ("Carl Zeiss Meditec", "AFX.DE"), ("CompuGroup Medical", "COP.DE"), ("CTS Eventim", "EVD.DE"),
    ("Delivery Hero", "DHER.DE"), ("Deutsche Pfandbriefbank", "PBB.DE"), ("Drägerwerk AG", "DRW3.DE"),
    ("DWS Group", "DWS.DE"), ("Encavis AG", "ECV.DE"), ("Evonik Industries", "EVK.DE"),
    ("Fraport AG", "FRA.DE"), ("Fuchs Petrolub", "FPE3.DE"), ("Gerresheimer AG", "GXI.DE"),
    ("GEA Group", "G1A.DE"), ("HELLA GmbH", "HLE.DE"), ("HUGO BOSS", "BOSS.DE"),
    ("K+S AG", "SDF.DE"), ("Kion Group", "KGX.DE"), ("Knorr-Bremse", "KBX.DE"),
    ("LANXESS AG", "LXS.DE"), ("LEG Immobilien", "LEG.DE"), ("Lufthansa AG", "LHA.DE"),
    ("MorphoSys AG", "MOR.DE"), ("Nemetschek SE", "NEM.DE"), ("Nordex SE", "NDX1.DE"),
    ("OSRAM Licht", "OSR.DE"), ("Rational AG", "RAA.DE"), ("Salzgitter AG", "SZG.DE"),
    ("Scout24 SE", "G24.DE"), ("Software AG", "SOW.DE"), ("Stroer SE", "SAX.DE"),
    ("Talanx AG", "TLX.DE"), ("ThyssenKrupp AG", "TKA.DE"), ("United Internet", "UTDI.DE"),
    ("Wacker Chemie", "WCH.DE"), ("Wacker Neuson", "WAC.DE"),
]

# =============================================================================
# UK — FTSE 100
# =============================================================================
FTSE100 = [
    ("Anglo American", "AAL.L"), ("Associated British Foods", "ABF.L"), ("Admiral Group", "ADM.L"),
    ("Ashtead Group", "AHT.L"), ("Antofagasta plc", "ANTO.L"), ("Aviva plc", "AV.L"),
    ("AstraZeneca plc", "AZN.L"), ("BAE Systems plc", "BA.L"), ("Barclays plc", "BARC.L"),
    ("British American Tobacco", "BATS.L"), ("Barratt Developments", "BDEV.L"), ("Beazley plc", "BEZ.L"),
    ("BHP Group", "BHP.L"), ("Berkeley Group", "BKG.L"), ("British Land", "BLND.L"),
    ("B&M European Value Retail", "BME.L"), ("Bunzl plc", "BNZL.L"), ("BP plc", "BP.L"),
    ("Burberry Group", "BRBY.L"), ("BT Group", "BT-A.L"), ("Coca-Cola HBC", "CCH.L"),
    ("Centrica plc", "CNA.L"), ("Compass Group", "CPG.L"), ("Croda Intl", "CRDA.L"),
    ("CRH plc", "CRH.L"), ("DCC plc", "DCC.L"), ("Diageo plc", "DGE.L"),
    ("Experian plc", "EXPN.L"), ("Fresnillo plc", "FRES.L"), ("Glencore plc", "GLEN.L"),
    ("GSK plc", "GSK.L"), ("Hikma Pharmaceuticals", "HIK.L"), ("Hargreaves Lansdown", "HL.L"),
    ("Halma plc", "HLMA.L"), ("HSBC Holdings", "HSBA.L"), ("Intl Consolidated Airlines", "IAG.L"),
    ("Intermediate Capital Group", "ICP.L"), ("InterContinental Hotels", "IHG.L"), ("3i Group", "III.L"),
    ("Imperial Brands", "IMB.L"), ("Intertek Group", "ITRK.L"), ("ITV plc", "ITV.L"),
    ("JD Sports Fashion", "JD.L"), ("Just Eat Takeaway", "JET.L"), ("Kingfisher plc", "KGF.L"),
    ("Land Securities Group", "LAND.L"), ("Legal & General Group", "LGEN.L"), ("Lloyds Banking Group", "LLOY.L"),
    ("London Stock Exchange Group", "LSEG.L"), ("Melrose Industries", "MRO.L"), ("Mondi plc", "MNDI.L"),
    ("M&G plc", "MNG.L"), ("National Grid plc", "NG.L"), ("NatWest Group", "NWG.L"),
    ("Next plc", "NXT.L"), ("Ocado Group", "OCDO.L"), ("Phoenix Group Holdings", "PHNX.L"),
    ("Prudential plc", "PRU.L"), ("Persimmon plc", "PSN.L"), ("Pearson plc", "PSON.L"),
    ("Relx plc", "REL.L"), ("Rio Tinto plc", "RIO.L"), ("Reckitt Benckiser Group", "RKT.L"),
    ("Rightmove plc", "RMV.L"), ("Rolls-Royce Holdings", "RR.L"), ("Rentokil Initial", "RTO.L"),
    ("Sainsbury (J) plc", "SBRY.L"), ("Schroders plc", "SDR.L"), ("Sage Group", "SGE.L"),
    ("Segro plc", "SGRO.L"), ("Shell plc", "SHEL.L"), ("Smith (DS) plc", "SMDS.L"),
    ("Smiths Group", "SMIN.L"), ("Scottish Mortgage Inv. Trust", "SMT.L"), ("Smith & Nephew", "SN.L"),
    ("Spirax-Sarco Engineering", "SPX.L"), ("SSE plc", "SSE.L"), ("Standard Chartered", "STAN.L"),
    ("St James's Place", "STJ.L"), ("Severn Trent", "SVT.L"), ("Tesco plc", "TSCO.L"),
    ("Taylor Wimpey", "TW.L"), ("Unilever plc", "ULVR.L"), ("United Utilities Group", "UU.L"),
    ("Vodafone Group", "VOD.L"), ("Weir Group", "WEIR.L"), ("WPP plc", "WPP.L"),
    ("Whitbread plc", "WTB.L"), ("F&C Investment Trust", "FCIT.L"), ("Smurfit Kappa Group", "SKG.L"),
    ("Pershing Square Holdings", "PSH.L"), ("Endeavour Mining", "EDV.L"), ("Entain plc", "ENT.L"),
    ("Auto Trader Group", "AUTO.L"), ("Marks & Spencer Group", "MKS.L"), ("Frasers Group", "FRAS.L"),
    ("Tritax Big Box REIT", "BBOX.L"), ("Howden Joinery Group", "HWDN.L"), ("Convatec Group", "CTEC.L"),
    ("Vistry Group", "VTY.L"), ("Pets at Home", "PETS.L"), ("Spirax Group", "SPX.L"),
]

# =============================================================================
# NETHERLANDS — AEX 25
# =============================================================================
AEX = [
    ("Adyen NV", "ADYEN.AS"), ("Aegon Ltd.", "AGN.AS"), ("Ahold Delhaize", "AD.AS"),
    ("Akzo Nobel NV", "AKZA.AS"), ("ArcelorMittal SA", "MT.AS"), ("ASM International", "ASM.AS"),
    ("ASML Holding NV", "ASML.AS"), ("ASR Nederland", "ASRNL.AS"), ("BE Semiconductor Industries", "BESI.AS"),
    ("DSM-Firmenich AG", "DSFIR.AS"), ("Exor NV", "EXO.AS"), ("Heineken NV", "HEIA.AS"),
    ("IMCD NV", "IMCD.AS"), ("ING Groep NV", "INGA.AS"), ("KPN NV", "KPN.AS"),
    ("NN Group NV", "NN.AS"), ("Philips NV", "PHIA.AS"), ("Prosus NV", "PRX.AS"),
    ("Randstad NV", "RAND.AS"), ("Relx NV", "REN.AS"), ("Shell plc (NL)", "SHELL.AS"),
    ("UMG Universal Music Group", "UMG.AS"), ("Wolters Kluwer NV", "WKL.AS"), ("WeTransfer (WeTransfer NV)", "WETR.AS"),
    ("BAM Group", "BAMNB.AS"),
]

# =============================================================================
# BELGIUM — BEL 20
# =============================================================================
BEL20 = [
    ("Ackermans & van Haaren", "ACKB.BR"), ("AedifIca", "AED.BR"), ("Ageas SA", "AGS.BR"),
    ("Anheuser-Busch InBev", "ABI.BR"), ("Aperam SA", "APAM.AS"), ("Argenx SE", "ARGX.BR"),
    ("Azelis Group", "AZE.BR"), ("Barco NV", "BAR.BR"), ("Cofinimmo SA", "COFB.BR"),
    ("D'ieteren Group", "DIE.BR"), ("Elia Group", "ELI.BR"), ("Galapagos NV", "GLPG.BR"),
    ("GBL Groupe Bruxelles Lambert", "GBLB.BR"), ("KBC Group", "KBC.BR"), ("Lotus Bakeries", "LOTB.BR"),
    ("Melexis NV", "MELE.BR"), ("Proximus SA", "PROX.BR"), ("Sofina SA", "SOF.BR"),
    ("Solvay SA", "SOLB.BR"), ("UCB SA", "UCB.BR"), ("Umicore SA", "UMI.BR"),
    ("Warehouses De Pauw", "WDP.BR"),
]

# =============================================================================
# SPAIN — IBEX 35
# =============================================================================
IBEX35 = [
    ("Acciona SA", "ANA.MC"), ("ACS Actividades Constr.", "ACS.MC"), ("Acerinox SA", "ACX.MC"),
    ("Aena SME", "AENA.MC"), ("Amadeus IT Group", "AMS.MC"), ("ArcelorMittal SA (ES)", "MTS.MC"),
    ("Banco Bilbao Vizcaya (BBVA)", "BBVA.MC"), ("Banco Sabadell", "SAB.MC"), ("Banco Santander", "SAN.MC"),
    ("Bankinter SA", "BKT.MC"), ("CaixaBank SA", "CABK.MC"), ("Cellnex Telecom", "CLNX.MC"),
    ("Colonial (Inmobiliaria)", "COL.MC"), ("Enagás SA", "ENG.MC"), ("Endesa SA", "ELE.MC"),
    ("Ferrovial SA", "FER.MC"), ("Fluidra SA", "FDR.MC"), ("Grifols SA", "GRF.MC"),
    ("Iberdrola SA", "IBE.MC"), ("IAG (Intl Airlines)", "IAG.MC"), ("Indra Sistemas", "IDR.MC"),
    ("Inditex (Industria Diseño)", "ITX.MC"), ("Logista Holdings", "LOG.MC"), ("Mapfre SA", "MAP.MC"),
    ("Melia Hotels Intl", "MEL.MC"), ("Merlin Properties", "MRL.MC"), ("Naturgy Energy", "NTGY.MC"),
    ("Puig Brands BV", "PUIG.MC"), ("Redeia Corporación", "RED.MC"), ("Repsol SA", "REP.MC"),
    ("Rovi (Laboratorios)", "ROVI.MC"), ("Sacyr SA", "SCYR.MC"), ("Solaria Energía", "SLR.MC"),
    ("Telefónica SA", "TEF.MC"), ("Unicaja Banco", "UNI.MC"),
]

# =============================================================================
# ITALY — FTSE MIB
# =============================================================================
FTSE_MIB = [
    ("A2A SpA", "A2A.MI"), ("Amplifon SpA", "AMP.MI"), ("Assicurazioni Generali", "G.MI"),
    ("Azimut Holding", "AZM.MI"), ("Banca Mediolanum", "BMED.MI"), ("Banca Monte Paschi", "BMPS.MI"),
    ("Banca Popolare Sondrio", "BPSO.MI"), ("Banco BPM", "BAMI.MI"), ("BPER Banca", "BPE.MI"),
    ("Brunello Cucinelli", "BC.MI"), ("Buzzi SpA", "BZU.MI"), ("Campari Group", "CPR.MI"),
    ("Diasorin SpA", "DIA.MI"), ("Enel SpA", "ENEL.MI"), ("Eni SpA", "ENI.MI"),
    ("Ferrari NV", "RACE.MI"), ("FinecoBank SpA", "FBK.MI"), ("Generali (Assicurazioni)", "G.MI"),
    ("Hera SpA", "HER.MI"), ("Inwit SpA", "INW.MI"), ("Intesa Sanpaolo", "ISP.MI"),
    ("Italgas SpA", "IG.MI"), ("Iveco Group", "IVG.MI"), ("Leonardo SpA", "LDO.MI"),
    ("Mediobanca SpA", "MB.MI"), ("Moncler SpA", "MONC.MI"), ("Nexi SpA", "NEXI.MI"),
    ("Pirelli & C.", "PIRC.MI"), ("Poste Italiane", "PST.MI"), ("Prysmian SpA", "PRY.MI"),
    ("Recordati SpA", "REC.MI"), ("Saipem SpA", "SPM.MI"), ("Snam SpA", "SRG.MI"),
    ("Stellantis NV", "STLAM.MI"), ("STMicroelectronics", "STM.MI"), ("Telecom Italia", "TIT.MI"),
    ("Tenaris SA", "TEN.MI"), ("Terna SpA", "TRN.MI"), ("UniCredit SpA", "UCG.MI"),
    ("Unipol Gruppo", "UNI.MI"),
]

# =============================================================================
# SWITZERLAND — SMI + selected SLI mid-caps
# =============================================================================
SWISS = [
    ("ABB Ltd.", "ABBN.SW"), ("Alcon Inc.", "ALC.SW"), ("Geberit AG", "GEBN.SW"),
    ("Givaudan SA", "GIVN.SW"), ("Holcim Ltd.", "HOLN.SW"), ("Kuehne + Nagel Intl", "KNIN.SW"),
    ("Logitech Intl", "LOGN.SW"), ("Lonza Group", "LONN.SW"), ("Nestlé SA", "NESN.SW"),
    ("Novartis AG", "NOVN.SW"), ("Partners Group", "PGHN.SW"), ("Richemont (Cie Financière)", "CFR.SW"),
    ("Roche Holding AG", "ROG.SW"), ("Sika AG", "SIKA.SW"), ("Sonova Holding", "SOON.SW"),
    ("Sunrise Communications", "SUNN.SW"), ("Swiss Life Holding", "SLHN.SW"), ("Swiss Re AG", "SREN.SW"),
    ("Swisscom AG", "SCMN.SW"), ("UBS Group AG", "UBSG.SW"), ("Zurich Insurance Group", "ZURN.SW"),
    ("Adecco Group", "ADEN.SW"), ("Baloise Holding", "BALN.SW"), ("Barry Callebaut", "BARN.SW"),
    ("Clariant AG", "CLN.SW"), ("Dufry AG", "DUFN.SW"), ("Ems-Chemie Holding", "EMSN.SW"),
    ("Helvetia Holding", "HELN.SW"), ("Julius Bär Gruppe", "BAER.SW"), ("Kühne + Nagel (alt)", "KNIN.SW"),
    ("Schindler Holding", "SCHN.SW"), ("Straumann Holding", "STMN.SW"), ("Temenos AG", "TEMN.SW"),
    ("VAT Group", "VACN.SW"),
]

# =============================================================================
# NORDICS — Sweden / Norway / Denmark / Finland (selected large-caps)
# =============================================================================
NORDICS = [
    # Sweden — OMX Stockholm 30
    ("ABB Ltd. (SE)", "ABB.ST"), ("Alfa Laval AB", "ALFA.ST"), ("Assa Abloy AB", "ASSA-B.ST"),
    ("AstraZeneca PLC (SDB)", "AZN.ST"), ("Atlas Copco A", "ATCO-A.ST"), ("Atlas Copco B", "ATCO-B.ST"),
    ("Boliden AB", "BOL.ST"), ("Electrolux AB", "ELUX-B.ST"), ("Epiroc AB", "EPI-A.ST"),
    ("Ericsson AB", "ERIC-B.ST"), ("Essity AB", "ESSITY-B.ST"), ("Evolution AB", "EVO.ST"),
    ("Getinge AB", "GETI-B.ST"), ("H&M Hennes & Mauritz", "HM-B.ST"), ("Hexagon AB", "HEXA-B.ST"),
    ("Investor AB", "INVE-B.ST"), ("Kinnevik AB", "KINV-B.ST"), ("Nibe Industrier", "NIBE-B.ST"),
    ("Nordea Bank Abp", "NDA-SE.ST"), ("Sandvik AB", "SAND.ST"), ("SCA Svenska Cellulosa", "SCA-B.ST"),
    ("SEB Skandinaviska Enskilda", "SEB-A.ST"), ("Securitas AB", "SECU-B.ST"), ("Skanska AB", "SKA-B.ST"),
    ("Sinch AB", "SINCH.ST"), ("SKF AB", "SKF-B.ST"), ("SSAB AB", "SSAB-A.ST"),
    ("Svenska Handelsbanken", "SHB-A.ST"), ("Swedbank AB", "SWED-A.ST"), ("Tele2 AB", "TEL2-B.ST"),
    ("Telia Company AB", "TELIA.ST"), ("Volvo AB", "VOLV-B.ST"),
    # Norway — OBX
    ("Aker BP ASA", "AKRBP.OL"), ("DNB Bank ASA", "DNB.OL"), ("Equinor ASA", "EQNR.OL"),
    ("Frontline plc", "FRO.OL"), ("Gjensidige Forsikring", "GJF.OL"), ("Kongsberg Gruppen", "KOG.OL"),
    ("Mowi ASA", "MOWI.OL"), ("Norsk Hydro", "NHY.OL"), ("Orkla ASA", "ORK.OL"),
    ("Schibsted SE", "SCHA.OL"), ("Stolt-Nielsen Ltd.", "SNI.OL"), ("Storebrand ASA", "STB.OL"),
    ("Telenor ASA", "TEL.OL"), ("Tomra Systems", "TOM.OL"), ("Yara International", "YAR.OL"),
    # Denmark — OMXC25
    ("A.P. Moller-Maersk A", "MAERSK-A.CO"), ("A.P. Moller-Maersk B", "MAERSK-B.CO"),
    ("Ambu A/S", "AMBU-B.CO"), ("Bavarian Nordic", "BAVA.CO"), ("Carlsberg A/S", "CARL-B.CO"),
    ("Chr. Hansen Holding", "CHR.CO"), ("Coloplast A/S", "COLO-B.CO"), ("Danske Bank A/S", "DANSKE.CO"),
    ("Demant A/S", "DEMANT.CO"), ("DSV A/S", "DSV.CO"), ("Genmab A/S", "GMAB.CO"),
    ("GN Store Nord", "GN.CO"), ("ISS A/S", "ISS.CO"), ("Jyske Bank A/S", "JYSK.CO"),
    ("Netcompany Group", "NETC.CO"), ("NKT A/S", "NKT.CO"), ("Novo Nordisk A/S", "NOVO-B.CO"),
    ("Novozymes A/S", "NZYM-B.CO"), ("Orsted A/S", "ORSTED.CO"), ("Pandora A/S", "PNDORA.CO"),
    ("Rockwool A/S", "ROCK-B.CO"), ("Royal Unibrew A/S", "RBREW.CO"), ("SimCorp A/S", "SIM.CO"),
    ("Tryg A/S", "TRYG.CO"), ("Vestas Wind Systems", "VWS.CO"), ("Zealand Pharma", "ZEAL.CO"),
    # Finland — OMXH25
    ("Elisa Oyj", "ELISA.HE"), ("Fortum Oyj", "FORTUM.HE"), ("Kesko Oyj A", "KESKOA.HE"),
    ("Kesko Oyj B", "KESKOB.HE"), ("Kone Oyj", "KNEBV.HE"), ("Konecranes Oyj", "KCR.HE"),
    ("Metso Oyj", "METSO.HE"), ("Neste Oyj", "NESTE.HE"), ("Nokia Oyj", "NOKIA.HE"),
    ("Nokian Tyres", "TYRES.HE"), ("Nordea Bank Abp (FI)", "NDA-FI.HE"), ("Orion Oyj", "ORNBV.HE"),
    ("Outokumpu Oyj", "OUT1V.HE"), ("Sampo plc", "SAMPO.HE"), ("Stora Enso Oyj", "STERV.HE"),
    ("UPM-Kymmene Oyj", "UPM.HE"), ("Wartsila Oyj", "WRT1V.HE"),
]

# =============================================================================
# IRELAND — ISEQ 20 (selected)
# =============================================================================
IRELAND = [
    ("AIB Group plc", "AIBG.IR"), ("Bank of Ireland Group", "BIRG.IR"), ("CRH plc (IE)", "CRH.IR"),
    ("Dalata Hotel Group", "DAL.IR"), ("FBD Holdings", "FBD.IR"), ("Glanbia plc", "GL9.IR"),
    ("Glenveagh Properties", "GVR.IR"), ("Greencoat Renewables", "GRP.IR"), ("Hostelworld Group", "HSW.IR"),
    ("Irish Continental Group", "IR5B.IR"), ("Kenmare Resources", "KMR.IR"), ("Kerry Group plc", "KRZ.IR"),
    ("Kingspan Group plc", "KRX.IR"), ("Origin Enterprises", "OIZ.IR"), ("PTSB (Permanent TSB)", "PTSB.IR"),
    ("Ryanair Holdings plc", "RYA.IR"), ("Smurfit Westrock (IE)", "SW3.IR"), ("Total Produce", "TOT.IR"),
    ("Uniphar plc", "UPR.IR"),
]

# =============================================================================
# AUSTRIA — ATX (selected)
# =============================================================================
AUSTRIA = [
    ("Andritz AG", "ANDR.VI"), ("BAWAG Group", "BG.VI"), ("CA Immobilien Anlagen", "CAI.VI"),
    ("DO & CO AG", "DOC.VI"), ("Erste Group Bank", "EBS.VI"), ("EVN AG", "EVN.VI"),
    ("Lenzing AG", "LNZ.VI"), ("Mayr-Melnhof Karton", "MMK.VI"), ("OMV AG", "OMV.VI"),
    ("Österreichische Post", "POST.VI"), ("Raiffeisen Bank Intl", "RBI.VI"), ("Schoeller-Bleckmann", "SBO.VI"),
    ("Strabag SE", "STR.VI"), ("Telekom Austria", "TKA.VI"), ("Verbund AG", "VER.VI"),
    ("Vienna Insurance Group", "VIG.VI"), ("Voestalpine AG", "VOE.VI"), ("Wienerberger AG", "WIE.VI"),
]

# =============================================================================
# JAPAN — Nikkei 225 selected large-caps
# =============================================================================
JAPAN = [
    ("Toyota Motor Corp.", "7203.T"), ("Sony Group Corp.", "6758.T"), ("Mitsubishi UFJ Financial", "8306.T"),
    ("Keyence Corp.", "6861.T"), ("SoftBank Group", "9984.T"), ("Tokyo Electron", "8035.T"),
    ("Recruit Holdings", "6098.T"), ("Hitachi Ltd.", "6501.T"), ("Honda Motor Co.", "7267.T"),
    ("Nintendo Co.", "7974.T"), ("Mitsubishi Corp.", "8058.T"), ("Itochu Corp.", "8001.T"),
    ("Sumitomo Mitsui Financial", "8316.T"), ("KDDI Corp.", "9433.T"), ("Mizuho Financial Group", "8411.T"),
    ("Nippon Telegraph & Telephone", "9432.T"), ("Fast Retailing (Uniqlo)", "9983.T"), ("Mitsui & Co.", "8031.T"),
    ("Daikin Industries", "6367.T"), ("Murata Manufacturing", "6981.T"), ("Shin-Etsu Chemical", "4063.T"),
    ("Disco Corp.", "6146.T"), ("Advantest Corp.", "6857.T"), ("Renesas Electronics", "6723.T"),
    ("Lasertec Corp.", "6920.T"), ("Tokyo Electric Power", "9501.T"), ("Chubu Electric Power", "9502.T"),
    ("Eneos Holdings", "5020.T"), ("INPEX Corp.", "1605.T"), ("Idemitsu Kosan", "5019.T"),
    ("JR East (East Japan Railway)", "9020.T"), ("JR Central (Central Japan Railway)", "9022.T"),
    ("ANA Holdings", "9202.T"), ("Japan Airlines", "9201.T"), ("Nippon Steel", "5401.T"),
    ("JFE Holdings", "5411.T"), ("Komatsu Ltd.", "6301.T"), ("Mitsubishi Heavy Industries", "7011.T"),
    ("Kawasaki Heavy Industries", "7012.T"), ("Subaru Corp.", "7270.T"), ("Suzuki Motor", "7269.T"),
    ("Nissan Motor", "7201.T"), ("Bridgestone Corp.", "5108.T"), ("Asahi Group Holdings", "2502.T"),
    ("Kirin Holdings", "2503.T"), ("Suntory Beverage & Food", "2587.T"), ("Ajinomoto Co.", "2802.T"),
    ("Kao Corp.", "4452.T"), ("Shiseido Co.", "4911.T"), ("Astellas Pharma", "4503.T"),
    ("Takeda Pharmaceutical", "4502.T"), ("Daiichi Sankyo", "4568.T"), ("Eisai Co.", "4523.T"),
    ("Chugai Pharmaceutical", "4519.T"), ("Olympus Corp.", "7733.T"), ("Terumo Corp.", "4543.T"),
    ("Hoya Corp.", "7741.T"), ("Canon Inc.", "7751.T"), ("Nikon Corp.", "7731.T"),
    ("Ricoh Co.", "7752.T"), ("Brother Industries", "6448.T"), ("Panasonic Holdings", "6752.T"),
    ("Sharp Corp.", "6753.T"), ("Toshiba Corp.", "6502.T"), ("Fujitsu Ltd.", "6702.T"),
    ("NEC Corp.", "6701.T"), ("Yokogawa Electric", "6841.T"), ("Omron Corp.", "6645.T"),
    ("Yaskawa Electric", "6506.T"), ("Fanuc Corp.", "6954.T"), ("SMC Corp.", "6273.T"),
    ("Denso Corp.", "6902.T"), ("Aisin Corp.", "7259.T"), ("Toyota Industries", "6201.T"),
    ("Yamaha Motor", "7272.T"), ("Yamaha Corp.", "7951.T"), ("Capcom Co.", "9697.T"),
    ("Bandai Namco Holdings", "7832.T"), ("Konami Group", "9766.T"), ("Square Enix Holdings", "9684.T"),
    ("Z Holdings (LINE)", "4689.T"), ("Rakuten Group", "4755.T"), ("Mercari Inc.", "4385.T"),
]

# =============================================================================
# HONG KONG / CHINA — Hang Seng + ADRs
# =============================================================================
CHINA_HK = [
    ("Tencent Holdings", "0700.HK"), ("Alibaba Group Holding", "9988.HK"), ("HSBC Holdings (HK)", "0005.HK"),
    ("AIA Group", "1299.HK"), ("Meituan", "3690.HK"), ("China Construction Bank", "0939.HK"),
    ("ICBC Industrial Commercial Bank", "1398.HK"), ("Ping An Insurance", "2318.HK"),
    ("CNOOC Ltd.", "0883.HK"), ("Bank of China", "3988.HK"), ("China Mobile", "0941.HK"),
    ("PetroChina Co.", "0857.HK"), ("Sinopec (China Petroleum)", "0386.HK"), ("BYD Company", "1211.HK"),
    ("Xiaomi Corp.", "1810.HK"), ("Geely Automobile", "0175.HK"), ("Li Auto Inc.", "2015.HK"),
    ("NIO Inc. (HK)", "9866.HK"), ("Xpeng Motors (HK)", "9868.HK"), ("Hong Kong Exchanges", "0388.HK"),
    ("Sun Hung Kai Properties", "0016.HK"), ("CK Asset Holdings", "1113.HK"), ("CK Hutchison Holdings", "0001.HK"),
    ("Galaxy Entertainment", "0027.HK"), ("Sands China", "1928.HK"), ("MGM China Holdings", "2282.HK"),
    ("Wynn Macau Ltd.", "1128.HK"), ("Power Assets Holdings", "0006.HK"), ("CLP Holdings", "0002.HK"),
    ("Hang Seng Bank", "0011.HK"), ("Bank of East Asia", "0023.HK"), ("BOC Hong Kong", "2388.HK"),
    ("Standard Chartered (HK)", "2888.HK"), ("Jardine Matheson", "JM.SI"), ("Cathay Pacific Airways", "0293.HK"),
    ("Swire Pacific A", "0019.HK"), ("MTR Corp.", "0066.HK"), ("Hong Kong & China Gas", "0003.HK"),
    ("China Resources Power", "0836.HK"), ("Anta Sports Products", "2020.HK"), ("Li Ning Co.", "2331.HK"),
    ("JD.com Inc. (HK)", "9618.HK"), ("Baidu Inc. (HK)", "9888.HK"), ("NetEase Inc. (HK)", "9999.HK"),
    ("KE Holdings (Beike)", "2423.HK"), ("Trip.com Group (HK)", "9961.HK"), ("Pinduoduo (PDD HK)", "9911.HK"),
    ("Kuaishou Technology", "1024.HK"), ("Bilibili Inc. (HK)", "9626.HK"), ("Tencent Music (HK)", "1698.HK"),
    # US ADRs of major Chinese names
    ("Alibaba Group ADR", "BABA"), ("JD.com ADR", "JD"), ("Baidu ADR", "BIDU"),
    ("NetEase ADR", "NTES"), ("NIO Inc. ADR", "NIO"), ("Li Auto ADR", "LI"),
    ("Xpeng Motors ADR", "XPEV"), ("Trip.com ADR", "TCOM"), ("Bilibili ADR", "BILI"),
    ("Yum China Holdings", "YUMC"), ("Vipshop Holdings", "VIPS"), ("Weibo Corp.", "WB"),
]

# =============================================================================
# KOREA — KOSPI selected
# =============================================================================
KOREA = [
    ("Samsung Electronics", "005930.KS"), ("SK Hynix", "000660.KS"), ("LG Energy Solution", "373220.KS"),
    ("Samsung Biologics", "207940.KS"), ("Hyundai Motor", "005380.KS"), ("Kia Corp.", "000270.KS"),
    ("POSCO Holdings", "005490.KS"), ("Naver Corp.", "035420.KS"), ("Kakao Corp.", "035720.KS"),
    ("Samsung SDI", "006400.KS"), ("LG Chem", "051910.KS"), ("LG Electronics", "066570.KS"),
    ("Hanwha Aerospace", "012450.KS"), ("Celltrion Inc.", "068270.KS"), ("Shinhan Financial Group", "055550.KS"),
    ("KB Financial Group", "105560.KS"), ("Hana Financial Group", "086790.KS"), ("Woori Financial Group", "316140.KS"),
    ("Korea Electric Power", "015760.KS"), ("Samsung C&T", "028260.KS"), ("Samsung Life Insurance", "032830.KS"),
    ("Samsung Fire & Marine", "000810.KS"), ("KT Corp.", "030200.KS"), ("SK Telecom", "017670.KS"),
    ("LG Uplus", "032640.KS"), ("Hyundai Mobis", "012330.KS"), ("Hyundai Steel", "004020.KS"),
    ("S-Oil Corp.", "010950.KS"), ("SK Innovation", "096770.KS"), ("Lotte Chemical", "011170.KS"),
    ("Hanwha Solutions", "009830.KS"), ("Doosan Enerbility", "034020.KS"), ("Kakao Pay", "377300.KS"),
    ("Krafton Inc.", "259960.KS"), ("Coupang Inc. (US listed)", "CPNG"),
]

# =============================================================================
# AUSTRALIA — ASX 50 selected
# =============================================================================
AUSTRALIA = [
    ("BHP Group Ltd.", "BHP.AX"), ("Commonwealth Bank of Australia", "CBA.AX"), ("CSL Limited", "CSL.AX"),
    ("Westpac Banking", "WBC.AX"), ("National Australia Bank", "NAB.AX"), ("ANZ Group Holdings", "ANZ.AX"),
    ("Macquarie Group", "MQG.AX"), ("Wesfarmers Ltd.", "WES.AX"), ("Woolworths Group", "WOW.AX"),
    ("Telstra Group", "TLS.AX"), ("Rio Tinto Ltd.", "RIO.AX"), ("Fortescue Metals Group", "FMG.AX"),
    ("Newcrest Mining (Newmont)", "NEM.AX"), ("Goodman Group", "GMG.AX"), ("Aristocrat Leisure", "ALL.AX"),
    ("Cochlear Ltd.", "COH.AX"), ("ResMed Inc. (AU)", "RMD.AX"), ("James Hardie Industries", "JHX.AX"),
    ("QBE Insurance Group", "QBE.AX"), ("Suncorp Group", "SUN.AX"), ("Insurance Australia Group", "IAG.AX"),
    ("AMP Ltd.", "AMP.AX"), ("Origin Energy", "ORG.AX"), ("Santos Ltd.", "STO.AX"),
    ("Woodside Energy", "WDS.AX"), ("South32 Ltd.", "S32.AX"), ("Mineral Resources", "MIN.AX"),
    ("Pilbara Minerals", "PLS.AX"), ("Allkem Ltd.", "AKE.AX"), ("Coles Group", "COL.AX"),
    ("Endeavour Group", "EDV.AX"), ("Treasury Wine Estates", "TWE.AX"), ("a2 Milk Company", "A2M.AX"),
    ("Bega Cheese", "BGA.AX"), ("Domino's Pizza (AU)", "DMP.AX"), ("Flight Centre Travel", "FLT.AX"),
    ("Qantas Airways", "QAN.AX"), ("Sydney Airport", "SYD.AX"), ("Transurban Group", "TCL.AX"),
    ("Atlassian Corp. (US)", "TEAM"), ("REA Group", "REA.AX"), ("Carsales.com", "CAR.AX"),
    ("Seek Ltd.", "SEK.AX"), ("Computershare Ltd.", "CPU.AX"), ("ASX Ltd.", "ASX.AX"),
    ("Stockland", "SGP.AX"), ("Mirvac Group", "MGR.AX"), ("Scentre Group", "SCG.AX"),
    ("Dexus", "DXS.AX"), ("GPT Group", "GPT.AX"), ("Charter Hall Group", "CHC.AX"),
]

# =============================================================================
# INDIA — major NSE listings (Yahoo .NS)
# =============================================================================
INDIA = [
    ("Reliance Industries", "RELIANCE.NS"), ("Tata Consultancy Services", "TCS.NS"),
    ("HDFC Bank", "HDFCBANK.NS"), ("Infosys Ltd.", "INFY.NS"), ("ICICI Bank", "ICICIBANK.NS"),
    ("Hindustan Unilever", "HINDUNILVR.NS"), ("Bharti Airtel", "BHARTIARTL.NS"), ("ITC Limited", "ITC.NS"),
    ("State Bank of India", "SBIN.NS"), ("Larsen & Toubro", "LT.NS"), ("Kotak Mahindra Bank", "KOTAKBANK.NS"),
    ("Axis Bank", "AXISBANK.NS"), ("Asian Paints", "ASIANPAINT.NS"), ("Maruti Suzuki India", "MARUTI.NS"),
    ("HCL Technologies", "HCLTECH.NS"), ("Bajaj Finance", "BAJFINANCE.NS"), ("Wipro Ltd.", "WIPRO.NS"),
    ("Mahindra & Mahindra", "M&M.NS"), ("Sun Pharmaceutical", "SUNPHARMA.NS"), ("Titan Company", "TITAN.NS"),
    ("UltraTech Cement", "ULTRACEMCO.NS"), ("Nestle India", "NESTLEIND.NS"), ("PowerGrid Corp.", "POWERGRID.NS"),
    ("NTPC Limited", "NTPC.NS"), ("Tech Mahindra", "TECHM.NS"), ("Tata Motors", "TATAMOTORS.NS"),
    ("Tata Steel", "TATASTEEL.NS"), ("Coal India", "COALINDIA.NS"), ("Adani Enterprises", "ADANIENT.NS"),
    ("Adani Ports", "ADANIPORTS.NS"), ("Adani Power", "ADANIPOWER.NS"), ("JSW Steel", "JSWSTEEL.NS"),
    ("Bharat Petroleum", "BPCL.NS"), ("Hindalco Industries", "HINDALCO.NS"), ("Bajaj Auto", "BAJAJ-AUTO.NS"),
    ("Hero MotoCorp", "HEROMOTOCO.NS"), ("Eicher Motors", "EICHERMOT.NS"), ("Cipla Ltd.", "CIPLA.NS"),
    ("Dr. Reddy's Labs", "DRREDDY.NS"), ("Divis Laboratories", "DIVISLAB.NS"),
    # US ADRs of Indian companies
    ("Infosys ADR", "INFY"), ("Wipro ADR", "WIT"), ("HDFC Bank ADR", "HDB"),
    ("ICICI Bank ADR", "IBN"), ("Tata Motors ADR", "TTM"), ("Dr. Reddy's ADR", "RDY"),
]

# =============================================================================
# LATAM — Brazil / Mexico large-caps
# =============================================================================
LATAM = [
    # Brazil — Bovespa
    ("Petrobras (Petróleo Brasileiro)", "PETR4.SA"), ("Vale SA", "VALE3.SA"), ("Itaú Unibanco Holding", "ITUB4.SA"),
    ("Bradesco SA", "BBDC4.SA"), ("Banco do Brasil", "BBAS3.SA"), ("Ambev SA", "ABEV3.SA"),
    ("Itausa SA", "ITSA4.SA"), ("WEG SA", "WEGE3.SA"), ("Magazine Luiza", "MGLU3.SA"),
    ("B3 SA Brasil Bolsa Balcão", "B3SA3.SA"), ("Eletrobras (Centrais Elétricas)", "ELET3.SA"),
    ("Suzano SA", "SUZB3.SA"), ("JBS SA", "JBSS3.SA"), ("BRF SA", "BRFS3.SA"),
    ("Klabin SA", "KLBN11.SA"), ("Embraer SA", "EMBR3.SA"), ("Localiza Rent a Car", "RENT3.SA"),
    ("Lojas Renner", "LREN3.SA"), ("Natura & Co.", "NTCO3.SA"), ("CSN (Cia Siderúrgica)", "CSNA3.SA"),
    ("Usiminas (Usinas Siderúrgicas)", "USIM5.SA"), ("CCR SA", "CCRO3.SA"), ("Cosan SA", "CSAN3.SA"),
    ("Rumo Logística", "RAIL3.SA"), ("Hapvida", "HAPV3.SA"), ("MercadoLibre (LatAm parent)", "MELI"),
    # US ADRs of Brazilian companies
    ("Petrobras ADR", "PBR"), ("Vale SA ADR", "VALE"), ("Itaú Unibanco ADR", "ITUB"),
    ("Bradesco ADR", "BBD"), ("Banco Santander Brasil", "BSBR"), ("Ambev ADR", "ABEV"),
    ("Embraer ADR", "ERJ"), ("XP Inc.", "XP"), ("StoneCo Ltd.", "STNE"),
    ("PagSeguro Digital", "PAGS"), ("Nu Holdings (Nubank)", "NU"),
    # Mexico — IPC
    ("America Movil (L)", "AMXB.MX"), ("Walmart de México", "WALMEX.MX"), ("Grupo Bimbo", "BIMBOA.MX"),
    ("Femsa (Fomento Económico)", "FEMSAUBD.MX"), ("Cemex SAB", "CEMEXCPO.MX"), ("Coca-Cola Femsa", "KOFUBL.MX"),
    ("Grupo Televisa", "TLEVISACPO.MX"), ("Grupo Aeroportuario Pacífico", "GAPB.MX"),
    ("Inbursa (Grupo Financiero)", "GFINBURO.MX"), ("Banorte (Grupo Financiero)", "GFNORTEO.MX"),
    # US ADRs of Mexican companies
    ("America Movil ADR", "AMX"), ("Cemex ADR", "CX"), ("Grupo Televisa ADR", "TV"),
    ("Coca-Cola Femsa ADR", "KOF"), ("Grupo Aero Pacifico ADR", "PAC"),
    ("Grupo Aero Sureste ADR", "ASR"), ("Grupo Aero Centro ADR", "OMAB"),
]

# =============================================================================
# SOUTH AFRICA + MIDDLE EAST + TURKEY
# =============================================================================
EMEA_EXTRA = [
    # South Africa — JSE
    ("Naspers Ltd.", "NPN.JO"), ("FirstRand Ltd.", "FSR.JO"), ("Standard Bank Group", "SBK.JO"),
    ("Sasol Ltd.", "SOL.JO"), ("Anglo American (JSE)", "AGL.JO"), ("MTN Group", "MTN.JO"),
    ("Vodacom Group", "VOD.JO"), ("Discovery Ltd.", "DSY.JO"), ("Sanlam Ltd.", "SLM.JO"),
    ("Capitec Bank Holdings", "CPI.JO"), ("Bidvest Group", "BVT.JO"), ("Shoprite Holdings", "SHP.JO"),
    ("Anglo American Platinum", "AMS.JO"), ("Sibanye Stillwater", "SSW.JO"), ("Impala Platinum", "IMP.JO"),
    # South Africa US ADRs
    ("Sasol ADR", "SSL"), ("Gold Fields ADR", "GFI"), ("Harmony Gold ADR", "HMY"),
    ("AngloGold Ashanti", "AU"),
    # Israel — TASE / Nasdaq
    ("Bank Leumi le-Israel", "LUMI.TA"), ("Bank Hapoalim", "POLI.TA"), ("Teva Pharmaceutical", "TEVA"),
    ("CyberArk Software", "CYBR"), ("Check Point Software", "CHKP"), ("NICE Ltd.", "NICE"),
    ("Wix.com Ltd.", "WIX"), ("Fiverr Intl", "FVRR"), ("Monday.com Ltd.", "MNDY"),
    ("Tower Semiconductor", "TSEM"), ("Camtek Ltd.", "CAMT"),
    # Turkey — BIST 30 (limited Yahoo coverage)
    ("Akbank T.A.S.", "AKBNK.IS"), ("Türkiye Garanti Bankası", "GARAN.IS"), ("Türkiye İş Bankası", "ISCTR.IS"),
    ("Koç Holding", "KCHOL.IS"), ("Tüpraş", "TUPRS.IS"), ("Turkcell İletişim", "TCELL.IS"),
    ("BIM Birleşik Mağazaları", "BIMAS.IS"), ("Ereğli Demir Çelik", "EREGL.IS"),
]

# =============================================================================
# EMERGING & SE ASIA — Singapore, Indonesia, Thailand, Vietnam, Philippines
# =============================================================================
ASIA_EMERGING = [
    # Singapore — STI
    ("DBS Group Holdings", "D05.SI"), ("Oversea-Chinese Banking", "O39.SI"), ("United Overseas Bank", "U11.SI"),
    ("Singapore Telecom", "Z74.SI"), ("Singapore Airlines", "C6L.SI"), ("CapitaLand Investment", "9CI.SI"),
    ("CapitaLand Ascendas REIT", "A17U.SI"), ("Wilmar International", "F34.SI"), ("ST Engineering", "S63.SI"),
    ("Keppel Corp.", "BN4.SI"), ("Sembcorp Industries", "U96.SI"), ("Singtel (Singapore Telecom)", "Z74.SI"),
    # Indonesia — JKSE
    ("Bank Central Asia (BCA)", "BBCA.JK"), ("Bank Mandiri", "BMRI.JK"), ("Bank Rakyat Indonesia", "BBRI.JK"),
    ("Bank Negara Indonesia", "BBNI.JK"), ("Telkom Indonesia", "TLKM.JK"), ("Astra International", "ASII.JK"),
    ("Unilever Indonesia", "UNVR.JK"), ("Indofood Sukses Makmur", "INDF.JK"),
    # Thailand — SET
    ("PTT PCL", "PTT.BK"), ("Siam Commercial Bank", "SCB.BK"), ("Bangkok Bank", "BBL.BK"),
    ("CP All PCL", "CPALL.BK"), ("Airports of Thailand", "AOT.BK"),
    # Vietnam (limited Yahoo coverage), Philippines
    ("Vingroup JSC", "VIC.VN"), ("Vinhomes JSC", "VHM.VN"),
    ("SM Investments Corp.", "SM.PS"), ("PLDT Inc.", "TEL.PS"),
]

# =============================================================================
# MAJOR ETFs — US / EU / Global
# =============================================================================
ETFS = [
    # US broad market
    ("SPDR S&P 500 ETF Trust", "SPY"), ("iShares Core S&P 500", "IVV"), ("Vanguard S&P 500", "VOO"),
    ("Invesco QQQ Trust", "QQQ"), ("Invesco NASDAQ 100 ETF", "QQQM"), ("SPDR Dow Jones Industrial", "DIA"),
    ("iShares Russell 2000", "IWM"), ("Vanguard Total Stock Market", "VTI"), ("Vanguard Total World Stock", "VT"),
    ("Vanguard FTSE All-World ex-US", "VEU"), ("iShares MSCI EAFE", "EFA"), ("iShares Core MSCI Emerging", "IEMG"),
    ("Vanguard FTSE Emerging Markets", "VWO"), ("iShares MSCI ACWI", "ACWI"), ("iShares MSCI World", "URTH"),
    # Sectors (SPDR)
    ("Technology Select Sector SPDR", "XLK"), ("Financial Select Sector SPDR", "XLF"),
    ("Health Care Select Sector SPDR", "XLV"), ("Consumer Discretionary SPDR", "XLY"),
    ("Consumer Staples Select SPDR", "XLP"), ("Energy Select Sector SPDR", "XLE"),
    ("Industrial Select Sector SPDR", "XLI"), ("Materials Select Sector SPDR", "XLB"),
    ("Utilities Select Sector SPDR", "XLU"), ("Real Estate Select Sector SPDR", "XLRE"),
    ("Communication Services SPDR", "XLC"),
    # Style / Factor
    ("iShares Russell 1000 Growth", "IWF"), ("iShares Russell 1000 Value", "IWD"),
    ("Vanguard Growth ETF", "VUG"), ("Vanguard Value ETF", "VTV"),
    ("iShares MSCI USA Min Vol", "USMV"), ("Invesco S&P 500 Equal Weight", "RSP"),
    ("iShares Edge MSCI USA Quality", "QUAL"), ("iShares MSCI USA Momentum", "MTUM"),
    # Bonds
    ("iShares Core US Aggregate Bond", "AGG"), ("Vanguard Total Bond Market", "BND"),
    ("iShares 20+ Year Treasury Bond", "TLT"), ("iShares 7-10 Year Treasury", "IEF"),
    ("iShares 1-3 Year Treasury Bond", "SHY"), ("Vanguard Short-Term Treasury", "VGSH"),
    ("iShares iBoxx High Yield Corp.", "HYG"), ("iShares iBoxx Investment Grade", "LQD"),
    ("Vanguard Total Intl Bond", "BNDX"), ("iShares JPM USD Emerging Bond", "EMB"),
    # Commodity ETFs
    ("SPDR Gold Shares", "GLD"), ("iShares Gold Trust", "IAU"), ("SPDR Gold MiniShares", "GLDM"),
    ("iShares Silver Trust", "SLV"), ("Invesco DB Agriculture", "DBA"), ("United States Oil Fund", "USO"),
    ("United States Natural Gas", "UNG"), ("Invesco DB Commodity", "DBC"), ("Aberdeen Std Phys Platinum", "PPLT"),
    ("Aberdeen Std Phys Palladium", "PALL"), ("Aberdeen Std Phys Precious Metals", "GLTR"),
    # Thematic
    ("ARK Innovation ETF", "ARKK"), ("ARK Genomic Revolution", "ARKG"), ("ARK Next Generation Internet", "ARKW"),
    ("ARK Autonomous Tech & Robotics", "ARKQ"), ("Global X Robotics & AI", "BOTZ"),
    ("Global X Cybersecurity", "BUG"), ("iShares Expanded Tech-Software", "IGV"),
    ("First Trust Cloud Computing", "SKYY"), ("Global X Lithium & Battery Tech", "LIT"),
    ("Global X U.S. Infrastructure", "PAVE"), ("SPDR S&P Aerospace & Defense", "XAR"),
    ("iShares U.S. Aerospace & Defense", "ITA"), ("ProShares Bitcoin Strategy", "BITO"),
    ("iShares Bitcoin Trust", "IBIT"), ("Fidelity Wise Origin Bitcoin", "FBTC"),
    ("Grayscale Bitcoin Trust", "GBTC"), ("iShares Ethereum Trust", "ETHA"),
    # International equity
    ("iShares MSCI Japan", "EWJ"), ("iShares MSCI China", "MCHI"), ("KraneShares CSI China Internet", "KWEB"),
    ("iShares MSCI India", "INDA"), ("iShares MSCI Brazil", "EWZ"), ("iShares MSCI Mexico", "EWW"),
    ("iShares MSCI South Korea", "EWY"), ("iShares MSCI Taiwan", "EWT"), ("iShares MSCI Germany", "EWG"),
    ("iShares MSCI United Kingdom", "EWU"), ("iShares MSCI France", "EWQ"), ("iShares MSCI Italy", "EWI"),
    ("iShares MSCI Spain", "EWP"), ("iShares MSCI Netherlands", "EWN"), ("iShares MSCI Switzerland", "EWL"),
    ("iShares MSCI Australia", "EWA"), ("iShares MSCI Canada", "EWC"), ("iShares MSCI Saudi Arabia", "KSA"),
    ("iShares MSCI Eurozone", "EZU"), ("iShares Europe ETF", "IEV"), ("Vanguard FTSE Europe", "VGK"),
    # Leveraged / Inverse (selected)
    ("ProShares UltraPro QQQ (3x)", "TQQQ"), ("ProShares UltraPro Short QQQ (-3x)", "SQQQ"),
    ("Direxion Daily S&P 500 Bull 3X", "SPXL"), ("Direxion Daily S&P 500 Bear 3X", "SPXS"),
    ("ProShares Ultra S&P 500 (2x)", "SSO"), ("ProShares Short S&P 500 (-1x)", "SH"),
    ("Direxion Daily Semicond Bull 3X", "SOXL"), ("Direxion Daily Semicond Bear 3X", "SOXS"),
    # European-listed UCITS ETFs
    ("iShares Core S&P 500 UCITS", "CSPX.L"), ("iShares Core MSCI World UCITS", "SWDA.L"),
    ("Vanguard FTSE All-World UCITS", "VWRL.L"), ("Lyxor CAC 40 UCITS", "CAC.PA"),
    ("iShares Core DAX UCITS", "EXS1.DE"), ("Lyxor DAX (DR) UCITS", "DAXEX.DE"),
    ("iShares STOXX Europe 600 UCITS", "EXSA.DE"), ("Amundi MSCI World UCITS", "CW8.PA"),
    ("Amundi S&P 500 UCITS", "500.PA"), ("Amundi MSCI Emerging Mkts UCITS", "AEEM.PA"),
    ("iShares MSCI EM UCITS", "EIMI.L"), ("iShares Edge MSCI World Min Vol", "MVOL.AS"),
    ("iShares Global Clean Energy", "INRG.L"), ("iShares Global Aerospace & Defence", "DFND.L"),
    ("iShares Global Government Bond UCITS", "IGLO.L"),
]

# =============================================================================
# CRYPTOCURRENCIES — Top 50 by market cap (USD pairs)
# =============================================================================
CRYPTO = [
    ("Bitcoin", "BTC-USD"), ("Ethereum", "ETH-USD"), ("Tether USDt", "USDT-USD"),
    ("BNB (Binance Coin)", "BNB-USD"), ("Solana", "SOL-USD"), ("USD Coin", "USDC-USD"),
    ("XRP (Ripple)", "XRP-USD"), ("Cardano", "ADA-USD"), ("Dogecoin", "DOGE-USD"),
    ("Avalanche", "AVAX-USD"), ("TRON", "TRX-USD"), ("Toncoin", "TON11419-USD"),
    ("Polkadot", "DOT-USD"), ("Polygon (MATIC)", "MATIC-USD"), ("Litecoin", "LTC-USD"),
    ("Shiba Inu", "SHIB-USD"), ("Chainlink", "LINK-USD"), ("Bitcoin Cash", "BCH-USD"),
    ("Uniswap", "UNI7083-USD"), ("Stellar", "XLM-USD"), ("Cosmos", "ATOM-USD"),
    ("Monero", "XMR-USD"), ("Ethereum Classic", "ETC-USD"), ("Internet Computer", "ICP-USD"),
    ("Filecoin", "FIL-USD"), ("Hedera Hashgraph", "HBAR-USD"), ("Aptos", "APT21794-USD"),
    ("Arbitrum", "ARB11841-USD"), ("Optimism", "OP-USD"), ("Maker", "MKR-USD"),
    ("Aave", "AAVE-USD"), ("Algorand", "ALGO-USD"), ("Sui", "SUI20947-USD"),
    ("VeChain", "VET-USD"), ("The Graph", "GRT6719-USD"), ("Sandbox", "SAND-USD"),
    ("Decentraland", "MANA-USD"), ("Tezos", "XTZ-USD"), ("EOS", "EOS-USD"),
    ("Theta Network", "THETA-USD"), ("Axie Infinity", "AXS-USD"), ("Fantom", "FTM-USD"),
    ("Render", "RNDR-USD"), ("Pepe", "PEPE24478-USD"), ("Bonk", "BONK-USD"),
    ("Floki", "FLOKI-USD"), ("Worldcoin", "WLD-USD"), ("Injective", "INJ-USD"),
    ("Stacks", "STX4847-USD"), ("Kaspa", "KAS-USD"),
]

# =============================================================================
# GLOBAL INDICES
# =============================================================================
INDICES = [
    ("S&P 500", "^GSPC"), ("Dow Jones Industrial", "^DJI"), ("NASDAQ Composite", "^IXIC"),
    ("NASDAQ-100", "^NDX"), ("Russell 2000", "^RUT"), ("Russell 1000", "^RUI"),
    ("Russell 3000", "^RUA"), ("S&P MidCap 400", "^MID"), ("S&P SmallCap 600", "^SML"),
    ("Wilshire 5000", "^W5000"), ("VIX Volatility", "^VIX"), ("VVIX (Vol of VIX)", "^VVIX"),
    ("CAC 40", "^FCHI"), ("CAC Mid 60", "^CACMD"), ("SBF 120", "^SBF120"),
    ("DAX 40", "^GDAXI"), ("MDAX", "^MDAXI"), ("TecDAX", "^TECDAX"), ("SDAX", "^SDAXI"),
    ("FTSE 100", "^FTSE"), ("FTSE 250", "^FTMC"), ("FTSE All-Share", "^FTAS"),
    ("Euro Stoxx 50", "^STOXX50E"), ("STOXX Europe 600", "^STOXX"), ("AEX (Amsterdam)", "^AEX"),
    ("BEL 20 (Brussels)", "^BFX"), ("IBEX 35 (Madrid)", "^IBEX"), ("FTSE MIB (Milan)", "FTSEMIB.MI"),
    ("SMI (Switzerland)", "^SSMI"), ("ATX (Vienna)", "^ATX"), ("OMX Stockholm 30", "^OMX"),
    ("OMX Copenhagen 25", "^OMXC25"), ("OMX Helsinki 25", "^OMXH25"), ("OBX (Oslo)", "OBX.OL"),
    ("ISEQ (Ireland)", "^ISEQ"), ("WIG 20 (Warsaw)", "^WIG20"),
    ("Nikkei 225", "^N225"), ("TOPIX", "^TPX"), ("Hang Seng Index", "^HSI"),
    ("Hang Seng China Enterprises", "^HSCE"), ("Shanghai Composite", "000001.SS"),
    ("Shenzhen Component", "399001.SZ"), ("KOSPI", "^KS11"), ("Taiwan Weighted", "^TWII"),
    ("Nifty 50 (India)", "^NSEI"), ("BSE Sensex", "^BSESN"), ("ASX 200", "^AXJO"),
    ("All Ordinaries (AU)", "^AORD"), ("Bovespa (Brazil)", "^BVSP"), ("S&P/BMV IPC (Mexico)", "^MXX"),
    ("S&P/TSX Composite (Canada)", "^GSPTSE"), ("FTSE JSE Top 40", "JTOPI.JO"),
    ("Tel Aviv 35 (Israel)", "^TA125.TA"), ("BIST 100 (Turkey)", "XU100.IS"),
]

# =============================================================================
# COMMODITIES & FOREX (futures + spot)
# =============================================================================
COMMODITIES_FX = [
    # Commodity futures
    ("Gold Futures", "GC=F"), ("Silver Futures", "SI=F"), ("Copper Futures", "HG=F"),
    ("Platinum Futures", "PL=F"), ("Palladium Futures", "PA=F"), ("Crude Oil WTI", "CL=F"),
    ("Brent Crude Oil", "BZ=F"), ("Natural Gas", "NG=F"), ("Heating Oil", "HO=F"),
    ("Gasoline RBOB", "RB=F"), ("Corn Futures", "ZC=F"), ("Wheat Futures", "ZW=F"),
    ("Soybean Futures", "ZS=F"), ("Soybean Oil", "ZL=F"), ("Soybean Meal", "ZM=F"),
    ("Coffee Futures", "KC=F"), ("Cocoa Futures", "CC=F"), ("Sugar Futures", "SB=F"),
    ("Cotton Futures", "CT=F"), ("Orange Juice", "OJ=F"), ("Live Cattle", "LE=F"),
    ("Lean Hogs", "HE=F"), ("Lumber Futures", "LBR=F"), ("Rough Rice", "ZR=F"),
    # Forex (major pairs)
    ("EUR/USD", "EURUSD=X"), ("GBP/USD", "GBPUSD=X"), ("USD/JPY", "JPY=X"),
    ("USD/CHF", "CHF=X"), ("USD/CAD", "CAD=X"), ("AUD/USD", "AUDUSD=X"),
    ("NZD/USD", "NZDUSD=X"), ("EUR/GBP", "EURGBP=X"), ("EUR/JPY", "EURJPY=X"),
    ("EUR/CHF", "EURCHF=X"), ("GBP/JPY", "GBPJPY=X"), ("USD/CNY", "CNY=X"),
    ("USD/HKD", "HKD=X"), ("USD/SGD", "SGD=X"), ("USD/INR", "INR=X"),
    ("USD/MXN", "MXN=X"), ("USD/BRL", "BRL=X"), ("USD/ZAR", "ZAR=X"),
    ("USD/TRY", "TRY=X"), ("USD/SEK", "SEK=X"), ("USD/NOK", "NOK=X"),
    ("USD/DKK", "DKK=X"), ("USD/PLN", "PLN=X"), ("USD/RUB", "RUB=X"),
    # US Treasury yields
    ("US 10Y Treasury Yield", "^TNX"), ("US 30Y Treasury Yield", "^TYX"),
    ("US 5Y Treasury Yield", "^FVX"), ("US 13W T-Bill", "^IRX"),
]


# =============================================================================
# BUILD AGGREGATE DICTIONARY
# =============================================================================
def _build_db() -> dict[str, str]:
    """
    Merge all groups into a single dict keyed by `"Name (TICKER)"` format,
    matching the convention used in app.py's ASSET_DB.
    Later groups override earlier ones if a label collision occurs.
    """
    groups = [
        SP500, NASDAQ100_EXTRA,
        CAC40, SBF120_EXTRA,
        DAX40, MDAX_SELECTED,
        FTSE100,
        AEX, BEL20, IBEX35, FTSE_MIB, SWISS, NORDICS, IRELAND, AUSTRIA,
        JAPAN, CHINA_HK, KOREA, AUSTRALIA, INDIA,
        LATAM, EMEA_EXTRA, ASIA_EMERGING,
        ETFS, CRYPTO, INDICES, COMMODITIES_FX,
    ]
    out: dict[str, str] = {}
    for grp in groups:
        for name, ticker in grp:
            label = f"{name} ({ticker})"
            out[label] = ticker
    return out


EXTENDED_ASSETS: dict[str, str] = _build_db()

# Quick sanity log when this module is imported standalone
if __name__ == "__main__":
    print(f"EXTENDED_ASSETS contains {len(EXTENDED_ASSETS):,} unique entries.")
