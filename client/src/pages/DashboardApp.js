import { faker } from "@faker-js/faker";
// @mui
import { useTheme } from "@mui/material/styles";
import { Grid, Container, Typography } from "@mui/material";
// components
import Page from "../components/Page";
import Iconify from "../components/Iconify";
// sections
import {
  AppOrderTimeline,
  AppWebsiteVisits,
  AppWidgetSummary,
} from "../sections/@dashboard/app";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "src/components/LocalizationProvider";

// ----------------------------------------------------------------------

export default function DashboardApp() {
  const theme = useTheme();
  const t = useTranslation();
  const user = JSON.parse(localStorage.getItem("user"));
  const navigate = useNavigate();

  useEffect(() => {
    console.log(user);
    console.log(localStorage.getItem("user"));
    if (!user) {
      navigate("/login", { replace: true });
    }
  }, [navigate, user]);

  return (
    <Page title={t("sharedDashboard")}>
      <Container maxWidth="xl">
        <Typography variant="h4" sx={{ mb: 5 }}>
          {t("sharedWelcome")} {user && user.displayName}!
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title={t("sharedWeeklyEarnings")}
              total={7100}
              icon={"ant-design:dollar-circle-filled"}
            />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title={`${t("sharedVideosViewed")} (${t("sharedWeek")})`}
              total={131}
              color="info"
              icon={"ant-design:video-camera-filled"}
            />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title={t("sharedMonthlyEarnings")}
              total={60000}
              color="warning"
              icon={"ant-design:dollar-circle-filled"}
            />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title={`${t("sharedVideosViewed")} (${t("sharedMonth")})`}
              total={534}
              color="error"
              icon={"ant-design:video-camera-filled"}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={8}>
            <AppWebsiteVisits
              title={t("sharedEarningTrends")}
              subheader="(+43%) than last year"
              chartLabels={[
                "01/01/2023",
                "01/02/2023",
                "01/03/2023",
                "01/04/2023",
                "01/05/2023",
                "01/06/2023",
                "01/07/2023",
                "01/08/2023",
                "01/09/2023",
                "01/10/2023",
                "01/11/2023",
              ]}
              chartData={[
                {
                  name: "Earnings",
                  type: "area",
                  fill: "gradient",
                  data: [
                    3000, 1200, 7000, 33000, 45000, 35000, 30000, 52000, 59000,
                    36000, 39000,
                  ],
                },
              ]}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={4}>
            <AppOrderTimeline
              title={t("sharedCashflowTimeline")}
              list={[...Array(5)].map((_, index) => ({
                id: faker.datatype.uuid(),
                title: [
                  `${t("sharedEarned")} Tshs. 20,000`,
                  `${t("sharedWithdrew")} Tshs. 12,000`,
                  `${t("sharedWithdrew")} Tshs. 15,000`,
                  `${t("sharedEarned")} Tshs. 7,000`,
                  `${t("sharedEarned")} Tshs. 1,000`,
                ][index],
                type: `order${index + 1}`,
                time: faker.date.past(),
              }))}
            />
          </Grid>
        </Grid>
      </Container>
    </Page>
  );
}
