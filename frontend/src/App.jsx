import { useEffect, useMemo, useState } from "react";
import axios from "axios";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  AreaChart,
  Area,
} from "recharts";

import {
  LayoutDashboard,
  Users,
  Package,
  BarChart3,
  TrendingUp,
  ShoppingCart,
  IndianRupee,
  UserRoundCheck,
  AlertTriangle,
  Search,
  RefreshCw,
  Moon,
  Sun,
  Menu,
  X,
  Database,
  ShieldAlert,
  Globe2,
  Crown,
  LogOut,
} from "lucide-react";

const API = "http://127.0.0.1:8000";

function App() {
  const [kpis, setKpis] = useState(null);
  const [revenue, setRevenue] = useState([]);
  const [segments, setSegments] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [products, setProducts] = useState([]);
  const [countries, setCountries] = useState([]);
  const [churn, setChurn] = useState([]);
  const [riskCustomers, setRiskCustomers] = useState([]);

  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState("");

  const [darkMode, setDarkMode] = useState(false);
  const [mobileMenu, setMobileMenu] = useState(false);

  const [activeSection, setActiveSection] = useState("dashboard");
  const [search, setSearch] = useState("");
  const [countryFilter, setCountryFilter] = useState("All");

  const [lastUpdated, setLastUpdated] = useState(null);

  // --------------------------------------------------
  // LOAD DASHBOARD
  // --------------------------------------------------

  const loadDashboard = async (showRefresh = false) => {
    try {
      if (showRefresh) {
        setRefreshing(true);
      } else {
        setLoading(true);
      }

      setError("");

      const responses = await Promise.all([
        axios.get(`${API}/analytics/kpis`),
        axios.get(`${API}/analytics/revenue`),
        axios.get(`${API}/analytics/segments`),
        axios.get(`${API}/analytics/customers`),
        axios.get(`${API}/analytics/products`),
        axios.get(`${API}/analytics/countries`),
        axios.get(`${API}/analytics/churn`),
        axios.get(`${API}/analytics/churn/customers`),
      ]);

      setKpis(responses[0].data);
      setRevenue(responses[1].data);
      setSegments(responses[2].data);
      setCustomers(responses[3].data);
      setProducts(responses[4].data);
      setCountries(responses[5].data);
      setChurn(responses[6].data);
      setRiskCustomers(responses[7].data);

      setLastUpdated(new Date());
    } catch (err) {
      console.error(err);
      setError(
        "Unable to connect to the analytics API. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    loadDashboard();
  }, []);

  // --------------------------------------------------
  // FILTERS
  // --------------------------------------------------

  const availableCountries = useMemo(() => {
    return ["All", ...countries.map((item) => item.country)];
  }, [countries]);

  const filteredCustomers = useMemo(() => {
    return customers.filter((customer) => {
      const matchesSearch =
        customer.name?.toLowerCase().includes(search.toLowerCase()) ||
        customer.country?.toLowerCase().includes(search.toLowerCase());

      const matchesCountry =
        countryFilter === "All" || customer.country === countryFilter;

      return matchesSearch && matchesCountry;
    });
  }, [customers, search, countryFilter]);

  const filteredProducts = useMemo(() => {
    return products.filter((product) => {
      return (
        product.product_name
          ?.toLowerCase()
          .includes(search.toLowerCase()) ||
        product.category?.toLowerCase().includes(search.toLowerCase())
      );
    });
  }, [products, search]);

  // --------------------------------------------------
  // HELPERS
  // --------------------------------------------------

  const formatCurrency = (value) => {
    return `₹${Number(value || 0).toLocaleString("en-IN", {
      maximumFractionDigits: 0,
    })}`;
  };

  const formatNumber = (value) => {
    return Number(value || 0).toLocaleString("en-IN");
  };

  const scrollToSection = (section) => {
    setActiveSection(section);
    setMobileMenu(false);

    const element = document.getElementById(section);

    if (element) {
      element.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  };

  // --------------------------------------------------
  // CHART DATA
  // --------------------------------------------------

  const segmentChartData = segments.map((item) => ({
    name: item.segment,
    customers: item.customers,
  }));

  const churnChartData = churn.map((item) => ({
    name: item.risk_category,
    customers: item.customers,
    probability: item.avg_churn_probability,
    revenue: item.revenue_at_risk,
  }));

  const PIE_COLORS = [
    "#4f46e5",
    "#7c3aed",
    "#0891b2",
    "#059669",
    "#d97706",
    "#dc2626",
  ];

  // --------------------------------------------------
  // LOADING
  // --------------------------------------------------

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loading-content">
          <div className="loading-logo">CI</div>

          <div className="loading-spinner"></div>

          <h2>Customer Intelligence</h2>

          <p>Loading business analytics...</p>
        </div>
      </div>
    );
  }

  // --------------------------------------------------
  // ERROR
  // --------------------------------------------------

  if (error && !kpis) {
    return (
      <div className="error-screen">
        <div className="error-card">
          <div className="error-icon">
            <AlertTriangle size={35} />
          </div>

          <h2>Dashboard Connection Failed</h2>

          <p>{error}</p>

          <button
            className="primary-button"
            onClick={() => loadDashboard()}
          >
            <RefreshCw size={17} />
            Retry Connection
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className={darkMode ? "app dark" : "app"}>

      {/* ==========================================
          MOBILE HEADER
      ========================================== */}

      <div className="mobile-header">
        <div className="mobile-brand">
          <div className="logo-icon">CI</div>

          <div>
            <strong>Customer</strong>
            <span>Intelligence</span>
          </div>
        </div>

        <button
          className="icon-button"
          onClick={() => setMobileMenu(!mobileMenu)}
        >
          {mobileMenu ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      {/* ==========================================
          SIDEBAR
      ========================================== */}

      <aside className={mobileMenu ? "sidebar mobile-open" : "sidebar"}>

        <div className="logo">
          <div className="logo-icon">CI</div>

          <div>
            <strong>Customer</strong>
            <span>Intelligence</span>
          </div>
        </div>

        <div className="sidebar-label">
          MAIN MENU
        </div>

        <nav>

          <button
            className={
              activeSection === "dashboard"
                ? "nav-item active"
                : "nav-item"
            }
            onClick={() => scrollToSection("dashboard")}
          >
            <LayoutDashboard size={18} />
            Dashboard
          </button>

          <button
            className={
              activeSection === "customers"
                ? "nav-item active"
                : "nav-item"
            }
            onClick={() => scrollToSection("customers")}
          >
            <Users size={18} />
            Customers
          </button>

          <button
            className={
              activeSection === "products"
                ? "nav-item active"
                : "nav-item"
            }
            onClick={() => scrollToSection("products")}
          >
            <Package size={18} />
            Products
          </button>

          <button
            className={
              activeSection === "analytics"
                ? "nav-item active"
                : "nav-item"
            }
            onClick={() => scrollToSection("analytics")}
          >
            <BarChart3 size={18} />
            Analytics
          </button>

          <button
            className={
              activeSection === "churn"
                ? "nav-item active"
                : "nav-item"
            }
            onClick={() => scrollToSection("churn")}
          >
            <ShieldAlert size={18} />
            Churn Risk
          </button>

        </nav>

        <div className="sidebar-bottom">

          <div className="database-status">
            <span className="status-dot"></span>

            <div>
              <strong>Database</strong>
              <small>Connected</small>
            </div>
          </div>

          <button className="logout-button">
            <LogOut size={17} />
            Analytics Mode
          </button>

        </div>

      </aside>

      {/* ==========================================
          MAIN CONTENT
      ========================================== */}

      <main className="main">

        {/* TOP BAR */}

        <header className="topbar">

          <div>
            <div className="breadcrumb">
              Analytics / Dashboard
            </div>

            <h1>Business Overview</h1>

            <p>
              Customer intelligence & business analytics
            </p>
          </div>

          <div className="topbar-actions">

            <div className="live-badge">
              <span></span>
              Live Data
            </div>

            <button
              className="icon-button"
              onClick={() => setDarkMode(!darkMode)}
              title="Toggle theme"
            >
              {darkMode ? <Sun size={19} /> : <Moon size={19} />}
            </button>

            <button
              className="refresh-button"
              onClick={() => loadDashboard(true)}
              disabled={refreshing}
            >
              <RefreshCw
                size={17}
                className={refreshing ? "spin" : ""}
              />

              {refreshing ? "Refreshing..." : "Refresh"}
            </button>

          </div>

        </header>

        {/* ==========================================
            DASHBOARD
        ========================================== */}

        <section id="dashboard">

          {/* KPI CARDS */}

          <section className="kpi-grid">

            <div className="kpi-card">

              <div className="kpi-top">
                <div className="kpi-icon purple">
                  <Users size={21} />
                </div>

                <span className="kpi-trend">
                  +12.4%
                </span>
              </div>

              <div className="kpi-label">
                Total Customers
              </div>

              <div className="kpi-value">
                {formatNumber(kpis.total_customers)}
              </div>

              <div className="kpi-footer">
                <UserRoundCheck size={14} />
                Active customers
              </div>

            </div>

            <div className="kpi-card">

              <div className="kpi-top">
                <div className="kpi-icon blue">
                  <ShoppingCart size={21} />
                </div>

                <span className="kpi-trend">
                  +8.7%
                </span>
              </div>

              <div className="kpi-label">
                Total Orders
              </div>

              <div className="kpi-value">
                {formatNumber(kpis.total_orders)}
              </div>

              <div className="kpi-footer">
                <TrendingUp size={14} />
                Completed orders
              </div>

            </div>

            <div className="kpi-card">

              <div className="kpi-top">
                <div className="kpi-icon green">
                  <IndianRupee size={21} />
                </div>

                <span className="kpi-trend">
                  +15.2%
                </span>
              </div>

              <div className="kpi-label">
                Total Revenue
              </div>

              <div className="kpi-value">
                {formatCurrency(kpis.total_revenue)}
              </div>

              <div className="kpi-footer">
                <TrendingUp size={14} />
                Gross revenue
              </div>

            </div>

            <div className="kpi-card">

              <div className="kpi-top">
                <div className="kpi-icon orange">
                  <BarChart3 size={21} />
                </div>

                <span className="kpi-trend">
                  +5.3%
                </span>
              </div>

              <div className="kpi-label">
                Average Order Value
              </div>

              <div className="kpi-value">
                {formatCurrency(kpis.average_order_value)}
              </div>

              <div className="kpi-footer">
                <IndianRupee size={14} />
                Revenue per order
              </div>

            </div>

          </section>

          {/* ==========================================
              FILTER BAR
          ========================================== */}

          <div className="filter-bar">

            <div className="search-box">

              <Search size={18} />

              <input
                type="text"
                placeholder="Search customers, products..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />

              {search && (
                <button onClick={() => setSearch("")}>
                  <X size={15} />
                </button>
              )}

            </div>

            <div className="filter-group">

              <Globe2 size={17} />

              <select
                value={countryFilter}
                onChange={(e) =>
                  setCountryFilter(e.target.value)
                }
              >
                {availableCountries.map((country) => (
                  <option key={country} value={country}>
                    {country === "All"
                      ? "All Countries"
                      : country}
                  </option>
                ))}
              </select>

            </div>

            <div className="updated-time">
              Last updated:{" "}
              {lastUpdated
                ? lastUpdated.toLocaleTimeString()
                : "--"}
            </div>

          </div>

          {/* ==========================================
              CHARTS
          ========================================== */}

          <section id="analytics" className="charts-grid">

            {/* REVENUE */}

            <div className="panel large-panel">

              <div className="panel-header">

                <div>
                  <h2>Revenue Performance</h2>
                  <p>Monthly revenue trend</p>
                </div>

                <div className="panel-icon">
                  <TrendingUp size={18} />
                </div>

              </div>

              <ResponsiveContainer
                width="100%"
                height={330}
              >

                <AreaChart data={revenue}>

                  <defs>
                    <linearGradient
                      id="revenueGradient"
                      x1="0"
                      y1="0"
                      x2="0"
                      y2="1"
                    >
                      <stop
                        offset="5%"
                        stopColor="#4f46e5"
                        stopOpacity={0.25}
                      />

                      <stop
                        offset="95%"
                        stopColor="#4f46e5"
                        stopOpacity={0}
                      />
                    </linearGradient>
                  </defs>

                  <CartesianGrid
                    strokeDasharray="3 3"
                    vertical={false}
                  />

                  <XAxis
                    dataKey="month"
                    tick={{ fontSize: 11 }}
                  />

                  <YAxis
                    tick={{ fontSize: 11 }}
                  />

                  <Tooltip
                    formatter={(value) =>
                      formatCurrency(value)
                    }
                  />

                  <Area
                    type="monotone"
                    dataKey="revenue"
                    stroke="#4f46e5"
                    strokeWidth={3}
                    fill="url(#revenueGradient)"
                  />

                </AreaChart>

              </ResponsiveContainer>

            </div>

            {/* RFM */}

            <div className="panel">

              <div className="panel-header">

                <div>
                  <h2>Customer Segments</h2>
                  <p>RFM customer distribution</p>
                </div>

                <div className="panel-icon purple-icon">
                  <Crown size={18} />
                </div>

              </div>

              <ResponsiveContainer
                width="100%"
                height={330}
              >

                <PieChart>

                  <Pie
                    data={segmentChartData}
                    dataKey="customers"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    outerRadius={105}
                    innerRadius={65}
                    paddingAngle={3}
                  >

                    {segmentChartData.map(
                      (_, index) => (
                        <Cell
                          key={index}
                          fill={
                            PIE_COLORS[
                              index %
                                PIE_COLORS.length
                            ]
                          }
                        />
                      )
                    )}

                  </Pie>

                  <Tooltip />

                </PieChart>

              </ResponsiveContainer>

              <div className="segment-legend">

                {segments.slice(0, 6).map(
                  (segment, index) => (

                    <div
                      className="legend-item"
                      key={segment.segment}
                    >

                      <span
                        className="legend-dot"
                        style={{
                          background:
                            PIE_COLORS[
                              index %
                                PIE_COLORS.length
                            ],
                        }}
                      />

                      <span>
                        {segment.segment}
                      </span>

                      <strong>
                        {segment.customers}
                      </strong>

                    </div>

                  )
                )}

              </div>

            </div>

          </section>

          {/* ==========================================
              CUSTOMER INSIGHTS
          ========================================== */}

          <section className="insight-grid">

            <div className="insight-card">

              <div className="insight-icon">
                <Crown size={20} />
              </div>

              <div>
                <span>Top Customer Segment</span>

                <strong>
                  {segments.length > 0
                    ? segments[0].segment
                    : "--"}
                </strong>
              </div>

            </div>

            <div className="insight-card">

              <div className="insight-icon">
                <Globe2 size={20} />
              </div>

              <div>
                <span>Top Country</span>

                <strong>
                  {countries.length > 0
                    ? countries[0].country
                    : "--"}
                </strong>
              </div>

            </div>

            <div className="insight-card">

              <div className="insight-icon">
                <Package size={20} />
              </div>

              <div>
                <span>Best Product</span>

                <strong>
                  {products.length > 0
                    ? products[0].product_name
                    : "--"}
                </strong>
              </div>

            </div>

            <div className="insight-card danger">

              <div className="insight-icon">
                <ShieldAlert size={20} />
              </div>

              <div>
                <span>High Risk Customers</span>

                <strong>
                  {churn.find(
                    (item) =>
                      item.risk_category ===
                      "High Risk"
                  )?.customers || 0}
                </strong>
              </div>

            </div>

          </section>

        </section>

        {/* ==========================================
            CUSTOMERS
        ========================================== */}

        <section id="customers" className="panel section-panel">

          <div className="panel-header">

            <div>
              <h2>Top Customers</h2>

              <p>
                Highest customer spending
              </p>
            </div>

            <div className="table-count">
              {filteredCustomers.length} customers
            </div>

          </div>

          <div className="table-wrapper">

            <table>

              <thead>

                <tr>
                  <th>Customer</th>
                  <th>Country</th>
                  <th>Orders</th>
                  <th>Total Spent</th>
                </tr>

              </thead>

              <tbody>

                {filteredCustomers.map(
                  (customer) => (

                    <tr key={customer.customer_id}>

                      <td>

                        <div className="customer-cell">

                          <div className="avatar">
                            {customer.name
                              ?.charAt(0)
                              .toUpperCase()}
                          </div>

                          <div>
                            <strong>
                              {customer.name}
                            </strong>

                            <small>
                              ID #{customer.customer_id}
                            </small>
                          </div>

                        </div>

                      </td>

                      <td>
                        <span className="country-badge">
                          {customer.country}
                        </span>
                      </td>

                      <td>
                        {customer.orders}
                      </td>

                      <td>
                        <strong className="money">
                          {formatCurrency(
                            customer.total_spent
                          )}
                        </strong>
                      </td>

                    </tr>

                  )
                )}

              </tbody>

            </table>

          </div>

        </section>

        {/* ==========================================
            PRODUCTS
        ========================================== */}

        <section id="products" className="panel section-panel">

          <div className="panel-header">

            <div>
              <h2>Top Products</h2>

              <p>
                Best performing products
              </p>
            </div>

            <div className="table-count">
              {filteredProducts.length} products
            </div>

          </div>

          <div className="table-wrapper">

            <table>

              <thead>

                <tr>
                  <th>Product</th>
                  <th>Category</th>
                  <th>Units Sold</th>
                  <th>Revenue</th>
                </tr>

              </thead>

              <tbody>

                {filteredProducts.map(
                  (product) => (

                    <tr key={product.product_id}>

                      <td>

                        <div className="product-cell">

                          <div className="product-icon">
                            <Package size={18} />
                          </div>

                          <div>
                            <strong>
                              {product.product_name}
                            </strong>

                            <small>
                              Product #
                              {product.product_id}
                            </small>
                          </div>

                        </div>

                      </td>

                      <td>
                        <span className="category-badge">
                          {product.category}
                        </span>
                      </td>

                      <td>
                        {formatNumber(
                          product.units_sold
                        )}
                      </td>

                      <td>
                        <strong className="money">
                          {formatCurrency(
                            product.revenue
                          )}
                        </strong>
                      </td>

                    </tr>

                  )
                )}

              </tbody>

            </table>

          </div>

        </section>

        {/* ==========================================
            CHURN
        ========================================== */}

        <section id="churn">

          <div className="section-heading">

            <div>
              <h2>AI Churn Intelligence</h2>

              <p>
                Machine learning powered customer
                retention analysis
              </p>
            </div>

            <div className="ai-badge">
              <ShieldAlert size={15} />
              ML Powered
            </div>

          </div>

          {/* CHURN CARDS */}

          <div className="churn-grid">

            {churn.map((item) => (

              <div
                className={`churn-card ${
                  item.risk_category
                    .toLowerCase()
                    .replace(" ", "-")
                }`}
                key={item.risk_category}
              >

                <div className="churn-card-header">

                  <span>
                    {item.risk_category}
                  </span>

                  <ShieldAlert size={19} />

                </div>

                <div className="churn-number">
                  {formatNumber(item.customers)}
                </div>

                <div className="churn-label">
                  Customers
                </div>

                <div className="churn-stat">

                  <span>
                    Avg. Probability
                  </span>

                  <strong>
                    {item.avg_churn_probability}%
                  </strong>

                </div>

                <div className="churn-stat">

                  <span>
                    Revenue at Risk
                  </span>

                  <strong>
                    {formatCurrency(
                      item.revenue_at_risk
                    )}
                  </strong>

                </div>

              </div>

            ))}

          </div>

          {/* CHURN CHART */}

          <div className="panel churn-chart-panel">

            <div className="panel-header">

              <div>
                <h2>Churn Risk Distribution</h2>

                <p>
                  Predicted customer risk levels
                </p>
              </div>

            </div>

            <ResponsiveContainer
              width="100%"
              height={320}
            >

              <BarChart data={churnChartData}>

                <CartesianGrid
                  strokeDasharray="3 3"
                  vertical={false}
                />

                <XAxis dataKey="name" />

                <YAxis />

                <Tooltip />

                <Bar
                  dataKey="customers"
                  fill="#dc2626"
                  radius={[8, 8, 0, 0]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

          {/* HIGH RISK TABLE */}

          <div className="panel section-panel">

            <div className="panel-header">

              <div>
                <h2>
                  Highest Churn Risk Customers
                </h2>

                <p>
                  Customers requiring immediate
                  attention
                </p>
              </div>

              <div className="risk-header">
                <AlertTriangle size={16} />
                Priority Customers
              </div>

            </div>

            <div className="table-wrapper">

              <table>

                <thead>

                  <tr>
                    <th>Customer</th>
                    <th>Country</th>
                    <th>Recency</th>
                    <th>Orders</th>
                    <th>Spent</th>
                    <th>Churn Probability</th>
                    <th>Risk</th>
                  </tr>

                </thead>

                <tbody>

                  {riskCustomers.map(
                    (customer) => (

                      <tr
                        key={customer.customer_id}
                      >

                        <td>

                          <div className="customer-cell">

                            <div className="avatar danger-avatar">
                              {customer.name
                                ?.charAt(0)
                                .toUpperCase()}
                            </div>

                            <div>
                              <strong>
                                {customer.name}
                              </strong>

                              <small>
                                ID #
                                {customer.customer_id}
                              </small>
                            </div>

                          </div>

                        </td>

                        <td>
                          {customer.country}
                        </td>

                        <td>
                          {customer.recency} days
                        </td>

                        <td>
                          {customer.frequency}
                        </td>

                        <td>
                          {formatCurrency(
                            customer.monetary
                          )}
                        </td>

                        <td>

                          <div className="probability">

                            <div className="progress">
                              <div
                                className="progress-fill"
                                style={{
                                  width: `${
                                    customer.churn_probability *
                                    100
                                  }%`,
                                }}
                              ></div>
                            </div>

                            <span>
                              {(
                                customer.churn_probability *
                                100
                              ).toFixed(1)}
                              %
                            </span>

                          </div>

                        </td>

                        <td>

                          <span
                            className={
                              customer.risk_category ===
                              "High Risk"
                                ? "risk-badge high"
                                : "risk-badge medium"
                            }
                          >
                            {customer.risk_category}
                          </span>

                        </td>

                      </tr>

                    )
                  )}

                </tbody>

              </table>

            </div>

          </div>

        </section>

        {/* ==========================================
            COUNTRY PERFORMANCE
        ========================================== */}

        <section className="panel section-panel">

          <div className="panel-header">

            <div>
              <h2>Country Performance</h2>

              <p>
                Revenue and customer distribution
              </p>
            </div>

            <Globe2 size={20} />

          </div>

          <div className="country-grid">

            {countries.map((country) => (

              <div
                className="country-card"
                key={country.country}
              >

                <div className="country-top">

                  <div className="country-flag">
                    <Globe2 size={20} />
                  </div>

                  <h3>
                    {country.country}
                  </h3>

                </div>

                <div className="country-revenue">
                  {formatCurrency(country.revenue)}
                </div>

                <div className="country-metrics">

                  <div>
                    <span>Customers</span>
                    <strong>
                      {formatNumber(
                        country.customers
                      )}
                    </strong>
                  </div>

                  <div>
                    <span>Orders</span>
                    <strong>
                      {formatNumber(
                        country.orders
                      )}
                    </strong>
                  </div>

                </div>

              </div>

            ))}

          </div>

        </section>

        {/* ==========================================
            FOOTER
        ========================================== */}

        <footer className="footer">

          <div>
            <strong>
              Customer Intelligence Platform
            </strong>

            <span>
              Business Analytics • RFM • Machine Learning
            </span>
          </div>

          <div className="footer-tech">

            <span>
              <Database size={14} />
              FastAPI
            </span>

            <span>
              MySQL
            </span>

            <span>
              React
            </span>

            <span>
              ML
            </span>

          </div>

        </footer>

      </main>

    </div>
  );
}

export default App;