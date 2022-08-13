import { Link as RouterLink } from 'react-router-dom';
// material
import { Grid, Button, Container, Stack, Typography } from '@mui/material';
// components
import Page from '../components/Page';
import Iconify from '../components/Iconify';
import { AdCard, AdsSort, AdsSearch } from '../sections/@dashboard/ads';
// mock
import POSTS from '../_mock/ads';

export default function Ads() {
  return (
    <Page title="Dashboard: Ads">
      <Container>
        <Grid container spacing={3}>
          {POSTS.map((post, index) => (
            <AdCard key={post.id} post={post} index={index} />
          ))}
        </Grid>
      </Container>
    </Page>
  );
}
