import { Navigate, useRoutes } from "react-router-dom";
// layouts
import DashboardLayout from "./layouts/dashboard";
import LogoOnlyLayout from "./layouts/LogoOnlyLayout";
//
import Ads from "./pages/Ads";
import Login from "./pages/Login";
import NotFound from "./pages/Page404";
import Register from "./pages/Register";
import Products from "./pages/Products";
import DashboardApp from "./pages/DashboardApp";
import Withdrawals from "./pages/Withdrawals";

// ----------------------------------------------------------------------

export default function Router() {
  return useRoutes([
    {
      path: "/dashboard",
      element: <DashboardLayout />,
      children: [
        { path: "app", element: <DashboardApp /> },
        { path: "withdrawals", element: <Withdrawals /> },
        { path: "products", element: <Products /> },
        { path: "", element: <Ads /> },
      ],
    },
    {
      path: "/",
      element: <LogoOnlyLayout />,
      children: [
        { path: "/", element: <Navigate to="/login" /> },
        { path: "login", element: <Login /> },
        { path: "register", element: <Register /> },
        { path: "404", element: <NotFound /> },
        { path: "*", element: <Navigate to="/404" /> },
      ],
    },
    { path: "*", element: <Navigate to="/404" replace /> },
  ]);
}
