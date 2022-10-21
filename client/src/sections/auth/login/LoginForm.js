import * as Yup from "yup";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";

import { Link, Stack, InputAdornment, IconButton } from "@mui/material";
import { LoadingButton } from "@mui/lab";

import {
  FormProvider,
  RHFCheckbox,
  RHFTextField,
} from "../../../components/hook-form";
import { auth, db } from "src/firebase";
import { signInWithEmailAndPassword } from "firebase/auth";
import {  errorsActions, sessionActions } from "src/store";
import Iconify from "src/components/Iconify";
import { doc, getDoc } from "firebase/firestore";
import { useDispatch } from "react-redux";

export default function LoginForm() {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("Invalid email/password");

  const LoginSchema = Yup.object().shape({
    email: Yup.string()
      .email("Email must be a valid email address")
      .required("Email is required"),
    password: Yup.string().required("Password is required"),
  });

  const defaultValues = {
    email: "",
    password: "",
    remember: true,
  };

  const methods = useForm({
    resolver: yupResolver(LoginSchema),
    defaultValues,
  });

  const login = async (email, password) => {
    setIsLoading(true);
    await signInWithEmailAndPassword(auth, email, password).then(async (result) => {
      const user = {
        uid: result.user.uid,
        phoneNumber: result.user.phoneNumber,
        email: result.user.email,
        emailVerified: result.user.emailVerified,
        displayName: result.user.displayName,
        accessToken: result.user.accessToken,
      };

      const docRef = doc(db, "users", user.uid);
      await getDoc(docRef)
        .then((doc) => {
          //  user.firstName = docSnap.data();
          console.log(doc);

          dispatch(sessionActions.updateUser(user));
          updateUserInLocalStorage(user);
          navigate("/dashboard/");
        })
        .catch((error) => {
          dispatch(errorsActions.push(errorMessage));
        });
    }).catch((error) => {
      dispatch(errorsActions.push(errorMessage));
    });
    setIsLoading(false);
  };

  const {
    handleSubmit,
    formState: { isSubmitting },
  } = methods;

  return (
    <FormProvider
      methods={methods}
      onSubmit={handleSubmit(() => {
        setIsLoading(true);
        login(methods.getValues().email, methods.getValues().password);
        setIsLoading(false);
      })}
    >
      <Stack spacing={3}>
        <RHFTextField name="email" label="Email address" />

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

      <LoadingButton
        fullWidth
        size="large"
        type="submit"
        variant="contained"
        loading={isLoading}
      >
        Login
      </LoadingButton>
    </FormProvider>
  );

  function updateUserInLocalStorage(user) {
    console.log(user);
    localStorage.setItem("user", JSON.stringify(user));
    dispatch(sessionActions.updateUser(user));
  }
}
