import * as Yup from "yup";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";

import {
  Link,
  Stack,
  Container,
  Button,
  Slide,
  TextField,
} from "@mui/material";
import { LoadingButton } from "@mui/lab";

import { FormProvider, RHFCheckbox } from "../../../components/hook-form";
import { auth } from "src/firebase";
import { RecaptchaVerifier, signInWithPhoneNumber } from "firebase/auth";
import RHFPhoneField from "src/components/hook-form/RHFPhoneField";
import { useDispatch } from "react-redux";
import { sessionActions } from "src/store";

export default function LoginForm() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [loading, setLoading] = useState(false);
  const [displayOTPField, setDisplayOTPField] = useState(false);
  const [validOTP, setValidOTP] = useState(true);
  const [OTPValue, setOTPValue] = useState(null);
  const [confirmation, setConfirmation] = useState(null);

  const sendOTP = () => {
    setLoading(true);
    const appVerifier = new RecaptchaVerifier(
      "recaptcha-container",
      {
        size: "invisible",
        callback: (response) => {
          // onSubmit();
        },
      },
      auth
    );
    const phone = `+255${methods.getValues().phone}`;
    signInWithPhoneNumber(auth, phone, appVerifier)
      .then((result) => {
        setDisplayOTPField(true);
        setConfirmation(result);
      })
      .catch((error) => {
        // dispatch(errorActions.push(error));t
        console.error(error);
      });
    setLoading(false);
  };

  const login = (confirmationResult) => {
    confirmationResult
      .confirm(OTPValue)
      .then((result) => {
        const user = {
          uid: result.user.uid,
          phoneNumber: result.user.phoneNumber,
          email: result.user.email,
          emailVerified: result.user.emailVerified,
          displayName: result.user.displayName,
          accessToken: result.user.accessToken,
        };
        console.log(user);
        dispatch(sessionActions.updateUser(user));
        navigate("/dashboard/app");
      })
      .catch((error) => {
        setValidOTP(false);
        console.log(error);
      });
  };

  const LoginSchema = Yup.object().shape({
    phone: Yup.string()
      .required("Phone number is required")
      .trim()
      .length(9, "Phone number must be a valid one 767852123"),
  });

  const defaultValues = {
    phone: "",
    remember: true,
  };

  const methods = useForm({
    resolver: yupResolver(LoginSchema),
    defaultValues,
  });

  const {
    handleSubmit,
    formState: { isSubmitting },
  } = methods;

  const onSubmit = async () => {
    navigate("/dashboard", { replace: true });
  };

  return (
    <FormProvider methods={methods} onSubmit={handleSubmit(sendOTP)}>
      <Container>
        <Stack spacing={3}>
          <RHFPhoneField name="phone" label="Phone number" type="phone" />
        </Stack>

        <Stack
          direction="row"
          alignItems="center"
          justifyContent="space-between"
          sx={{ my: 2 }}
        >
          <RHFCheckbox name="remember" label="Remember me" />
          <Link variant="subtitle2" underline="hover">
            Forgot password?
          </Link>
        </Stack>

        <div id="recaptcha-container"></div>

        <LoadingButton
          fullWidth
          size="large"
          type="submit"
          variant="contained"
          loading={loading}
        >
          Login
        </LoadingButton>
      </Container>

      <Slide direction="up" in={displayOTPField} mountOnEnter unmountOnExit>
        <Container
          sx={{
            display: displayOTPField ? "block" : "none",
            mt: 4,
            width: "100%",
          }}
        >
          <Stack
            direction={"row"}
            alignContent={"stretch"}
            alignItems={"stretch"}
          >
            <TextField
              sx={{ mr: 4, textAlign: "center" }}
              error={!validOTP}
              helperText={
                validOTP
                  ? "Enter the code sent to you number"
                  : "You have entered a wrong code"
              }
              label="OTP Code"
              onChange={(e) => setOTPValue(e.target.value)}
            />
            <Button
              size="large"
              variant="contained"
              onClick={(e) => login(confirmation)}
            >
              Verify Code
            </Button>
          </Stack>
        </Container>
      </Slide>
    </FormProvider>
  );
}
