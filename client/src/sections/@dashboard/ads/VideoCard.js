import videojs from "video.js";

import POSTS from "../../../_mock/ads";
import { useEffect, useRef, useState } from "react";
import { Video } from "src/sections/@dashboard/ads/Video";
import BaseCard from "src/sections/@dashboard/ads/BaseCard";
import { formatAPIURL, formatStreamingURL } from "src/utils/formatUrl";
import { useDispatch, useSelector } from "react-redux";
import { watchedActions } from "src/store";

export default function VideoCard({ index, video }) {
  const playerRef = useRef(null);
  const dispatch = useDispatch();
  const [ready, setReady] = useState(false);
  const [display, setDisplay] = useState("block");
  const [play, setPlay] = useState(false);
  const watchedVideos = useSelector((state) => state.watched.items);

  const videoJsOptions = {
    autoplay: false,
    controls: false,
    responsive: true,
    fill: true,
    // fluid: true,
    sources: [
      {
        src: formatStreamingURL(video.uuid),
        type: "application/dash+xml",
      },
    ],
  };

  const markAsWatched = async (duration, currentTime, uuid) => {
    const percentage = currentTime / duration;

    if (percentage >= 0.02 && !watchedVideos.includes(uuid)) {
      console.log(`${uuid} watched`);
      const url = formatAPIURL("watch", video.uuid);
      dispatch(watchedActions.push(uuid));

      try {
        const response = await fetch(url, { method: "POST" });
        if (response.ok) {
          const data = await response.json();
          video = data;
        }
      } catch (e) {
        console.log(e);
      }
    }
  };

  const handlePlayerReady = (player) => {
    playerRef.current = player;

    // You can handle player events here, for example:
    player.on("play", () => {
      console.log(player.currentTime() / player.duration());
    });

    player.on("timeupdate", () => {
      markAsWatched(player.duration(), player.currentTime(), video.uuid);
    });

    player.on("waiting", () => {
      videojs.log("player is waiting");
    });

    player.on("ready", () => {
      setReady(true);
    });

    player.on("dispose", () => {
      videojs.log("player will dispose");
    });
  };

  useEffect(() => {
    const player = playerRef.current;
    try {
      if (play && player) {
        player.play();
      } else {
        player.pause();
      }
    } catch (e) {}
  }, [play, ready]);

  return (
    <BaseCard
      key={index}
      video={video}
      post={POSTS[index]}
      index={index}
      displayValue={display}
      togglePlay={() => {
        if (play) {
          setPlay(false);
          setDisplay("block");
        } else {
          setPlay(true);
          setDisplay("none");
        }
      }}
      fullScreenToggle={() => {
        const player = playerRef.current;
        if (player) {
          player.requestFullscreen();
        }
      }}
      media={<Video options={videoJsOptions} onReady={handlePlayerReady} />}
    />
  );
}
