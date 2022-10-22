import { Link as RouterLink, useNavigate } from "react-router-dom";
// @mui
import { styled } from "@mui/material/styles";
import { Card, Link, Container, Typography, Grid } from "@mui/material";
// hooks
import useResponsive from "../hooks/useResponsive";
// components
import Page from "../components/Page";
import Logo from "../components/Logo";
// sections
import { LoginForm } from "../sections/auth/login";
import AuthSocial from "../sections/auth/AuthSocial";
import constants from "src/components/constants";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { sessionActions } from "src/store";
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

export default function Login() {
  const smUp = useResponsive("up", "sm");
  const mdUp = useResponsive("up", "md");
  const t = useTranslation();

  const partialRegistration = useSelector(
    (state) => state.session.partialRegistration
  );

  return (
    <Page title="Login">
      <RootStyle>
        <HeaderStyle>
          <Logo />

          {smUp && (
            <Typography variant="body2" sx={{ mt: { md: -2 } }}>
              {t("loginDontHaveAnAccount")} {""}
              <Link variant="subtitle2" component={RouterLink} to="/register">
                {t("loginGetStarted")}
              </Link>
            </Typography>
          )}
        </HeaderStyle>

        <Container maxWidth="sm">
          <ContentStyle>
            {(partialRegistration && (
              <Typography variant="h4" gutterBottom>
                Continue your registration with your phone number
              </Typography>
            )) || (
              <Grid
                container
                direction="row"
                justifyContent="center"
                alignItems="center"
              >
                <Grid item xs={10}>
                  <Typography variant="h4" gutterBottom>
                    {t("loginSignInTo")} {constants.companyName}
                  </Typography>
                </Grid>
                <Grid item xs={2}>
                  <LanguagePopover />
                </Grid>
              </Grid>
            )}

            <Typography sx={{ color: "text.secondary", mb: 5 }}>
              {t("loginEnterYourDetailsBelow")}
            </Typography>

            {/* <AuthSocial /> */}

            <LoginForm />
            {!smUp && (
              <Typography variant="body2" align="center" sx={{ mt: 3 }}>
                {t("loginDontHaveAnAccount")}{" "}
                <Link variant="subtitle2" component={RouterLink} to="/register">
                  {t("loginGetStarted")}
                </Link>
              </Typography>
            )}
          </ContentStyle>
        </Container>
      </RootStyle>
    </Page>
  );
}
