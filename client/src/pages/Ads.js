import { Grid, Container } from "@mui/material";
// components
import Page from "../components/Page";
// mock
import POSTS from "../_mock/ads";
import VideoCard from "src/sections/@dashboard/ads/VideoCard";

export default function Ads() {
  const baseUrl = "http://app.thought.ninja";

  return (
    <Page title="Dashboard: Ads">
      <Container>
        <Grid container spacing={3}>
          <VideoCard
            index={0}
            url={`${baseUrl}/streaming/rpg/dash.mpd`}
            play={true}
          />
          <VideoCard
            index={1}
            url={`${baseUrl}/streaming/ariana_grande/dash.mpd`}
            play={true}
          />
          <VideoCard
            index={2}
            url={`${baseUrl}/streaming/big/dash.mpd`}
            play={true}
          />
          <VideoCard
            index={3}
            url={`${baseUrl}/streaming/rpg/dash.mpd`}
            play={true}
          />
          {/* {POSTS.map((post, index) => (
            <AdCard key={post.id} post={post} index={index} />
          ))} */}
        </Grid>
      </Container>
    </Page>
  );
}
