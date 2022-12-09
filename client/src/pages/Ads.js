import { Grid, Container, LinearProgress } from "@mui/material";
// components
import Page from "../components/Page";

import VideoCard from "src/sections/@dashboard/ads/VideoCard";
import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { errorsActions } from "src/store";
import { useEffectAsync } from "src/utils/helpers";
import { formatAPIURL } from "src/utils/formatUrl";

export default function Ads() {
  const dispatch = useDispatch();

  const [videos, setVideos] = useState([]);

  useEffectAsync(async () => {
    try {
      const url = formatAPIURL();
      const response = await fetch(url, { method: "GET" });
      const data = await response.json();
      console.table(data);
      setVideos(data);
    } catch (e) {
      console.log(e);
      dispatch(errorsActions.push("error"));
    }
  }, []);

  if (videos.length > 0) {
    return (
      <Page title="Dashboard: Ads">
        <Container>
          <Grid container spacing={3}>
            {videos.map((video, index) => (
              <VideoCard key={index} index={index} video={video} play={true} />
            ))}
          </Grid>
        </Container>
      </Page>
    );
  }

  return (
    <Page title="Dashboard: Ads">
      <LinearProgress />
    </Page>
  );
}
