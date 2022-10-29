import { Grid, Container, LinearProgress } from "@mui/material";
// components
import Page from "../components/Page";

import VideoCard from "src/sections/@dashboard/ads/VideoCard";
import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { errorsActions } from "src/store";
import { useEffectAsync } from "src/utils/helpers";

export default function Ads() {
  const dispatch = useDispatch();

  // const baseUrl = "http://app.thought.ninja";
  const baseUrl = "http://127.0.0.1:8001";
  const [videos, setVideos] = useState([]);

  useEffectAsync(async () => {
    try {
      const url = `${baseUrl}/api/ads/`;
      const response = await fetch(url, { method: "GET" });
      const data = await response.json();
      console.table(data);
      setVideos(data);
    } catch (e) {
      console.log(e);
      dispatch(errorsActions.push("error"));
    }
  }, [baseUrl]);

  if (videos.length > 0) {
    return (
      <Page title="Dashboard: Ads">
        <Container>
          <Grid container spacing={3}>
            {videos.map((video, index) => (
              <VideoCard
                key={index}
                index={index}
                url={`http://127.0.0.1/streaming/processed/${video.uuid}/dash.mpd`}
                play={true}
              />
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
