import * as Yup from "yup";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
// form
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
// @mui
import { IconButton, InputAdornment, Snackbar, Stack } from "@mui/material";
import { LoadingButton } from "@mui/lab";

import { FormProvider, RHFTextField } from "../../../components/hook-form";
import { useDispatch } from "react-redux";
import { errorsActions, registrationActions, sessionActions } from "src/store";
import Iconify from "src/components/Iconify";
import RHFPhoneField from "src/components/hook-form/RHFPhoneField";

import { doc, setDoc } from "firebase/firestore";
import {
  createUserWithEmailAndPassword,
  getAuth,
  updateProfile,
} from "firebase/auth";
import { db } from "src/firebase";

// ----------------------------------------------------------------------

export default function RegisterForm() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const auth = getAuth();

  const [emailExists, setEmailExists] = useState(false);
  const [isLoading, setIsLoading] = useState(false);


  const [showPassword, setShowPassword] = useState(false);

  const RegisterSchema = Yup.object().shape({
    firstName: Yup.string().required("First name required").min(3),
    lastName: Yup.string().required("Last name required").min(3),
    email: Yup.string()
      .email("Email must be a valid email address")
      .required("Email is required"),
    phone: Yup.string()
      .required("Phone number is required")
      .length(9, "Phone number must be a valid one"),
    password: Yup.string().required("Password is required"),
    password_confirm: Yup.string()
      .required("Password Confirmation is required")
      .oneOf([Yup.ref("password"), null], "Passwords must match"),
  });

  const defaultValues = {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
    password: "",
    password_confirm: "",
  };

  const methods = useForm({
    resolver: yupResolver(RegisterSchema),
    defaultValues,
  });

  const {
    handleSubmit,
    formState: { isSubmitting },
  } = methods;

  const onSubmit = async () => {
    const user = {};
    user.name = `${methods.getValues().firstName} ${
      methods.getValues().lastName
    }`;
    user.email = methods.getValues().email;
    user.displayName = methods.getValues().firstName;
    user.phone = methods.getValues().phone;
    user.firstName = methods.getValues().firstName;
    user.lastName = methods.getValues().lastName;
    user.password = methods.getValues().password;

    if (user.password === methods.getValues().password_confirm) {
      await setIsLoading(true);
      await createUserWithEmailAndPassword(auth, user.email, user.password).then(
        (userCredential) => {
          updateProfile(auth.currentUser, {
            email: user.email,
            displayName: user.displayName,
          })
            .then(async (result) => {
              setDoc(doc(db, "users", userCredential.user.uid), {
                user,
              }).then(() => {
                dispatch(sessionActions.updateUser(user));
                navigate("/login", { replace: true });
              }).catch((error) => dispatch(errorsActions.push(error.message)))
            })
            .catch((error) => {
              setEmailExists(true);
              dispatch(errorsActions.push("Email already exists, please use another email address!"));
            });
        }
      );
      await setIsLoading(false);
    }
  };

  return (
    <FormProvider methods={methods} onSubmit={handleSubmit(onSubmit)}>
      <Stack spacing={3}>
        <Stack direction={{ xs: "column", sm: "row" }} spacing={2}>
          <RHFTextField name="firstName" label="First name" />
          <RHFTextField name="lastName" label="Last name" />
        </Stack>
        <RHFPhoneField name="phone" label="Phone number" type="phone" />
        <RHFTextField name="email" label="Email address" />
        <Stack direction={{ xs: "column", sm: "row" }} spacing={2}>
          <RHFTextField
            name="password"
            label="Password"
            type={showPassword ? "text" : "password"}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    onClick={() => setShowPassword(!showPassword)}
                    edge="end"
                  >
                    <Iconify
                      icon={showPassword ? "eva:eye-fill" : "eva:eye-off-fill"}
                    />
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
          <RHFTextField
            name="password_confirm"
            label="Confirm Password"
            type={showPassword ? "text" : "password"}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    onClick={() => setShowPassword(!showPassword)}
                    edge="end"
                  >
                    <Iconify
                      icon={showPassword ? "eva:eye-fill" : "eva:eye-off-fill"}
                    />
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
        </Stack>
        <LoadingButton
          fullWidth
          size="large"
          type="submit"
          variant="contained"
          loading={isLoading}
        >
          Register
        </LoadingButton>
        {/* <Snackbar
          open={emailExists}
          autoHideDuration={6000}
          onClose={setEmailExists(false)}
          message={`Email is already used`}
        /> */}
      </Stack>
    </FormProvider>
  );
}
