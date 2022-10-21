import { useLayoutEffect, useRef, useState } from "react";
// material
import { alpha } from "@mui/material/styles";
import { Box, MenuItem, Stack, IconButton } from "@mui/material";
// components
import MenuPopover from "../../components/MenuPopover";
import { useLocalization } from "src/components/LocalizationProvider";


export default function LanguagePopover() {
  const { languages, language, setLanguage } = useLocalization();
  const [activeLang, setActiveLang] = useState(0);
  const languageList = Object.entries(languages).map((values) => ({
    code: values[0],
    name: values[1].name,
    icon: values[1].icon
  }));

  const anchorRef = useRef(null);
  const [open, setOpen] = useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  useLayoutEffect(() => {
    setActiveLang(languageList.findIndex((option) => option.code === language));
  }, [language, languageList, languages, setActiveLang]);

  return (
    <>
      <IconButton
        ref={anchorRef}
        onClick={handleOpen}
        sx={{
          padding: 0,
          width: 44,
          height: 44,
          ...(open && {
            bgcolor: (theme) =>
              alpha(
                theme.palette.primary.main,
                theme.palette.action.focusOpacity
              ),
          }),
        }}
      >
        <img src={languageList[activeLang].icon} alt={languageList[activeLang].label} />
      </IconButton>

      <MenuPopover
        open={open}
        onClose={handleClose}
        anchorEl={anchorRef.current}
        sx={{
          mt: 1.5,
          ml: 0.75,
          width: 180,
          "& .MuiMenuItem-root": {
            px: 1,
            typography: "body2",
            borderRadius: 0.75,
          },
        }}
      >
        <Stack spacing={0.75}>
          {languageList.map((option, index) => (
            <MenuItem
              key={index}
              value={index}
              selected={option.code === language}
              onClick={(e) => {
                const value = e.target.value;
                setLanguage(languageList[value].code);
                handleClose();
              }}
            >
              <Box
                component="img"
                alt={option.name}
                src={option.icon}
                sx={{ width: 28, mr: 2 }}
              />
              {option.name}
            </MenuItem>
          ))}
        </Stack>
      </MenuPopover>
    </>
  );
}
