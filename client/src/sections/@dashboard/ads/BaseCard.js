import PropTypes from "prop-types";
import { Link as RouterLink } from "react-router-dom";
// material
import { alpha, styled } from "@mui/material/styles";
import {
  Box,
  Link,
  Card,
  Grid,
  Avatar,
  Typography,
  CardContent,
  IconButton,
} from "@mui/material";
// utils
import { fDate } from "../../../utils/formatTime";
import { fShortenNumber } from "../../../utils/formatNumber";
//
import SvgIconStyle from "../../../components/SvgIconStyle";
import Iconify from "../../../components/Iconify";
import PlayCircleOutlineIcon from "@mui/icons-material/PlayCircleOutline";
import { Fullscreen } from "@mui/icons-material";

// ----------------------------------------------------------------------

const CardMediaStyle = styled("div")({
  position: "relative",
  paddingTop: "calc(100% * 3 / 4)",
});

const TitleStyle = styled(Link)({
  height: 44,
  overflow: "hidden",
  WebkitLineClamp: 2,
  display: "-webkit-box",
  WebkitBoxOrient: "vertical",
});

const AvatarStyle = styled(Avatar)(({ theme }) => ({
  zIndex: 9,
  width: 32,
  height: 32,
  position: "absolute",
  left: theme.spacing(3),
  bottom: theme.spacing(-2),
}));

const InfoStyle = styled("div")(({ theme }) => ({
  display: "flex",
  flexWrap: "wrap",
  justifyContent: "flex-end",
  marginTop: theme.spacing(3),
  color: theme.palette.text.disabled,
  zIndex: 8,
  left: theme.spacing(3),
  bottom: theme.spacing(-2),
}));

const CoverImgStyle = styled("div")({
  top: 0,
  width: "100%",
  height: "100%",
  objectFit: "cover",
  position: "absolute",
});

// ----------------------------------------------------------------------

BaseCard.propTypes = {
  post: PropTypes.object.isRequired,
  index: PropTypes.number,
};

export default function BaseCard({
  post,
  index,
  media,
  displayValue,
  togglePlay,
  fullScreenToggle,
}) {
  const { cover, title, view, comment, share, author, createdAt } = post;
  const latestPostLarge = index === 0;
  const latestPost = index === 1 || index === 2;

  const AD_INFO = [
    { number: view, icon: "eva:eye-fill" },
    { number: share, icon: "eva:share-fill" },
  ];

  return (
    <Grid item xs={12} sm={12} md={12}>
      <Card
        onClick={() => togglePlay()}
        sx={{
          position: "relative",
          mx: {
            md: "20%",
          },
        }}
      >
        <CardMediaStyle
          sx={{
            ...{
              pt: "calc(100% * 4 / 3)",
              "&:after": {
                top: 0,
                content: "''",
                width: "100%",
                height: "100%",
                position: "absolute",
                // bgcolor: (theme) => alpha(theme.palette.grey[900], 0.72),
              },
            },
            ...{
              pt: {
                xs: "calc(100% * 4 / 3)",
                sm: "calc(100% * 3 / 4.66)",
              },
            },
          }}
        >
          <SvgIconStyle
            color="paper"
            src="/static/icons/shape-avatar.svg"
            sx={{
              width: 80,
              height: 36,
              zIndex: 9,
              bottom: -15,
              position: "absolute",
              color: "background.paper",
              ...{ display: "none" },
            }}
          />
          <AvatarStyle
            alt={author.name}
            src={author.avatarUrl}
            sx={{
              ...{
                zIndex: 9,
                top: 24,
                left: 24,
                width: 40,
                height: 40,
                display: displayValue,
              },
            }}
          />

          <CoverImgStyle alt={title} src={cover} children={media} />
          <IconButton
            sx={{
              position: "absolute",
              top: "45%",
              left: "45%",
              zIndex: 1,
              display: displayValue,
            }}
          >
            <PlayCircleOutlineIcon fontSize="large" color="white" />
          </IconButton>
        </CardMediaStyle>

        <CardContent
          sx={{
            pt: 4,
            ...{
              bottom: 0,
              width: "100%",
              position: "absolute",
            },
          }}
        >
          <TitleStyle
            to="#"
            color="inherit"
            variant="subtitle2"
            underline="hover"
            component={RouterLink}
            sx={{
              ...{ typography: "h5", height: 60 },
              ...{
                color: "common.white",
              },
              display: displayValue,
            }}
          >
            {title}
          </TitleStyle>

          <InfoStyle>
            {AD_INFO.map((info, index) => (
              <Box
                key={index}
                sx={{
                  display: "flex",
                  alignItems: "center",
                  ml: index === 0 ? 0 : 1.5,
                  ...{
                    color: "grey.500",
                  },
                }}
              >
                <Iconify
                  icon={info.icon}
                  sx={{ width: 16, height: 16, mr: 0.5 }}
                />
                <Typography variant="caption">
                  {fShortenNumber(info.number)}
                </Typography>
              </Box>
            ))}
            <IconButton onClick={() => fullScreenToggle()}>
              <Fullscreen />
            </IconButton>
          </InfoStyle>
        </CardContent>
      </Card>
    </Grid>
  );
}
