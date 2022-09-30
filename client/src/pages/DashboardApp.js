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
import { useSelector } from "react-redux";

// ----------------------------------------------------------------------

export default function DashboardApp() {
  const theme = useTheme();
  const user = useSelector((state) => state.session.user);

  return (
    <Page title="Dashboard">
      <Container maxWidth="xl">
        <Typography variant="h4" sx={{ mb: 5 }}>
          Welcome {user && user.displayName}!
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title="Weekly Earnings"
              total={7100}
              icon={"ant-design:dollar-circle-filled"}
            />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title="Videos Viewed (Week)"
              total={131}
              color="info"
              icon={"ant-design:video-camera-filled"}
            />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title="Monthly Earnings"
              total={60000}
              color="warning"
              icon={"ant-design:dollar-circle-filled"}
            />
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <AppWidgetSummary
              title="Videos Views (Month)"
              total={534}
              color="error"
              icon={"ant-design:video-camera-filled"}
            />
          </Grid>

          <Grid item xs={12} md={6} lg={8}>
            <AppWebsiteVisits
              title="Earning Trends"
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
              title="Cashflow Timeline"
              list={[...Array(5)].map((_, index) => ({
                id: faker.datatype.uuid(),
                title: [
                  "Earned Tshs. 20,000",
                  "Withdrew Tshs. 12,000",
                  "Withdrew Tshs. 15,000",
                  "Earned Tshs. 7,000",
                  "Earned Tshs. 1,000",
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
