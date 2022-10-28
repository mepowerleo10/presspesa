// routes
import Router from "./routes";
// theme
import ThemeProvider from "./theme";
// components
import ScrollToTop from "./components/ScrollToTop";
import { BaseOptionChartStyle } from "./components/chart/BaseOptionChart";
import ErrorHandler from "./components/ErrorHandler";
import store from "./store";
import { Provider } from "react-redux";
import { LocalizationProvider } from "./components/LocalizationProvider";

// ----------------------------------------------------------------------

export default function App() {
  return (
    <Provider store={store}>
      <LocalizationProvider>
        <ThemeProvider>
          <ScrollToTop />
          <BaseOptionChartStyle />
          <Router />
          <ErrorHandler />
        </ThemeProvider>
      </LocalizationProvider>
    </Provider>
  );
}
