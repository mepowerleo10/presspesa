import { Link as RouterLink } from "react-router-dom";
// @mui
import { styled } from "@mui/material/styles";
import { Card, Link, Container, Typography, Grid } from "@mui/material";
// hooks
import useResponsive from "../hooks/useResponsive";
// components
import Page from "../components/Page";
import Logo from "../components/Logo";
// sections
import { RegisterForm } from "../sections/auth/register";
import AuthSocial from "../sections/auth/AuthSocial";
import constants from "src/components/constants";
import { useTranslation } from "src/components/LocalizationProvider";
import LanguagePopover from "src/layouts/dashboard/LanguagePopover";

// ----------------------------------------------------------------------

const RootStyle = styled("div")(({ theme }) => ({
  [theme.breakpoints.up("md")]: {
    display: "flex",
  },
}));

const HeaderStyle = styled("header")(({ theme }) => ({
  top: 0,
  zIndex: 9,
  lineHeight: 0,
  width: "100%",
  display: "flex",
  alignItems: "center",
  position: "absolute",
  padding: theme.spacing(3),
  justifyContent: "space-between",
  [theme.breakpoints.up("md")]: {
    alignItems: "flex-start",
    padding: theme.spacing(7, 5, 0, 7),
  },
}));

const SectionStyle = styled(Card)(({ theme }) => ({
  width: "100%",
  maxWidth: 464,
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  margin: theme.spacing(2, 0, 2, 2),
}));

const ContentStyle = styled("div")(({ theme }) => ({
  maxWidth: 480,
  margin: "auto",
  minHeight: "100vh",
  display: "flex",
  justifyContent: "center",
  flexDirection: "column",
  padding: theme.spacing(12, 0),
}));

// ----------------------------------------------------------------------

export default function Register() {
  const smUp = useResponsive("up", "sm");

  const mdUp = useResponsive("up", "md");
  const t = useTranslation();

  return (
    <Page title="Register">
      <RootStyle>
        <HeaderStyle>
          <Logo />
          {smUp && (
            <Typography variant="body2" sx={{ mt: { md: -2 } }}>
              {t("registerAlreadyHaveAnAccount")} {""}
              <Link variant="subtitle2" component={RouterLink} to="/login">
                {t("sharedLogin")}
              </Link>
            </Typography>
          )}
        </HeaderStyle>

        <Container>
          <ContentStyle>
            <Grid
              container
              direction="row"
              justifyContent="center"
              alignItems="center"
            >
              <Grid item xs={10}>
                <Typography variant="h4" gutterBottom>
                  {t("registerSignUpItIsAbsolutelyFree")}
                </Typography>
              </Grid>
              <Grid item xs={2}>
                <LanguagePopover />
              </Grid>
            </Grid>

            <Typography sx={{ color: "text.secondary", mb: 5 }}>
              {t("sharedNoCreditNeeded")}
            </Typography>

            {/* <AuthSocial /> */}

            <RegisterForm />

            <Typography
              variant="body2"
              align="center"
              sx={{ color: "text.secondary", mt: 3 }}
            >
              {t("sharedByRegisteringIAgreeTo")}{" "}
              <Link underline="always" color="text.primary" href="#">
                {t("sharedTermsOfService")}
              </Link>{" "}
              {t("sharedAnd")}{" "}
              <Link underline="always" color="text.primary" href="#">
                {t("sharedPrivacyPolicy")}
              </Link>
              .
            </Typography>

            {!smUp && (
              <Typography variant="body2" sx={{ mt: 3, textAlign: "center" }}>
                {t("registerAlreadyHaveAnAccount")} {""}
                <Link variant="subtitle2" to="/login" component={RouterLink}>
                  {t("sharedLogin")}
                </Link>
              </Typography>
            )}
          </ContentStyle>
        </Container>
      </RootStyle>
    </Page>
  );
}
