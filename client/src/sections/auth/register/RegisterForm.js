import * as Yup from "yup";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
// form
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
// @mui
import { Stack } from "@mui/material";
import { LoadingButton } from "@mui/lab";

import { FormProvider, RHFTextField } from "../../../components/hook-form";
import { useDispatch } from "react-redux";
import { registrationActions, sessionActions } from "src/store";

// ----------------------------------------------------------------------

export default function RegisterForm() {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const RegisterSchema = Yup.object().shape({
    firstName: Yup.string().required("First name required"),
    lastName: Yup.string().required("Last name required"),
    phone: Yup.string()
      .required("Phone number is required")
      .length(10, "Phone number must be a valid one"),
    password: Yup.string().required("Password is required"),
  });

  const defaultValues = {
    firstName: "",
    lastName: "",
    email: "",
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
    dispatch(registrationActions.updateUser(user));
    dispatch(sessionActions.updatePartialRegistration(true));
    navigate("/login", { replace: true });
  };

  return (
    <FormProvider methods={methods} onSubmit={onSubmit}>
      <Stack spacing={3}>
        <Stack direction={{ xs: "column", sm: "row" }} spacing={2}>
          <RHFTextField name="firstName" label="First name" />
          <RHFTextField name="lastName" label="Last name" />
        </Stack>

        <RHFTextField name="email" label="Email address" />

        <LoadingButton
          fullWidth
          size="large"
          type="submit"
          variant="contained"
          loading={isSubmitting}
        >
          Register
        </LoadingButton>
      </Stack>
    </FormProvider>
  );
}
