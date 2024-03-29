import { useRef, useState } from "react";
import { Link as RouterLink } from "react-router-dom";
// @mui
import { alpha } from "@mui/material/styles";
import {
  Box,
  Divider,
  Typography,
  Stack,
  MenuItem,
  Avatar,
  IconButton,
} from "@mui/material";
// components
import MenuPopover from "../../components/MenuPopover";
// mocks_
import account from "../../_mock/account";
import { useDispatch, useSelector } from "react-redux";
import { signOut } from "firebase/auth";
import { auth } from "src/firebase";
import { sessionActions } from "src/store";

// ----------------------------------------------------------------------

const MENU_OPTIONS = [
  {
    label: "Home",
    icon: "eva:home-fill",
    linkTo: "/dashboard/ads",
  },
  {
    label: "Profile",
    icon: "eva:person-fill",
    linkTo: "#",
  },
];

// ----------------------------------------------------------------------

export default function AccountPopover() {
  const anchorRef = useRef(null);

  const user = JSON.parse(localStorage.getItem("user"));
  const dispatch = useDispatch();

  const [open, setOpen] = useState(null);

  const handleOpen = (event) => {
    setOpen(event.currentTarget);
  };

  const handleClose = () => {
    setOpen(null);
    dispatch(sessionActions.updateUser(null));
    localStorage.removeItem("user");
    signOut(auth);
  };

  return (
    <>
      <IconButton
        ref={anchorRef}
        onClick={handleOpen}
        sx={{
          p: 0,
          ...(open && {
            "&:before": {
              zIndex: 1,
              content: "''",
              width: "100%",
              height: "100%",
              borderRadius: "50%",
              position: "absolute",
              bgcolor: (theme) => alpha(theme.palette.grey[900], 0.8),
            },
          }),
        }}
      >
        <Avatar src={account.photoURL} alt="photoURL" />
      </IconButton>

      <MenuPopover
        open={Boolean(open)}
        anchorEl={open}
        onClose={handleClose}
        sx={{
          p: 0,
          mt: 1.5,
          ml: 0.75,
          "& .MuiMenuItem-root": {
            typography: "body2",
            borderRadius: 0.75,
          },
        }}
      >
        {user && (
          <Box sx={{ my: 1.5, px: 2.5 }}>
            <Typography variant="subtitle2" noWrap>
              {user.displayName}
            </Typography>
            <Typography variant="body2" sx={{ color: "text.secondary" }} noWrap>
              {user.email}
            </Typography>
            <Typography variant="body2" sx={{ color: "text.secondary" }} noWrap>
              {user.phone}
            </Typography>
          </Box>
        )}

        <Divider sx={{ borderStyle: "dashed" }} />

        <Stack sx={{ p: 1 }}>
          {MENU_OPTIONS.map((option) => (
            <MenuItem
              key={option.label}
              to={option.linkTo}
              component={RouterLink}
              onClick={handleClose}
            >
              {option.label}
            </MenuItem>
          ))}
        </Stack>

        <Divider sx={{ borderStyle: "dashed" }} />

        <MenuItem
          onClick={handleClose}
          to={"/login"}
          component={RouterLink}
          sx={{ m: 1 }}
        >
          Logout
        </MenuItem>
      </MenuPopover>
    </>
  );
}
