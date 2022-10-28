import videojs from "video.js";

import POSTS from "../../../_mock/ads";
import { useEffect, useRef, useState } from "react";
import { Video } from "src/sections/@dashboard/ads/Video";
import BaseCard from "src/sections/@dashboard/ads/BaseCard";

export default function VideoCard({ index, url }) {
  const playerRef = useRef(null);
  const [ready, setReady] = useState(false);
  const [display, setDisplay] = useState("block");
  const [play, setPlay] = useState(false);

  console.log(url);

  const videoJsOptions = {
    autoplay: false,
    controls: false,
    responsive: true,
    fill: true,
    // fluid: true,
    sources: [
      {
        src: url,
        type: "application/dash+xml",
      },
    ],
  };

  const handlePlayerReady = (player) => {
    playerRef.current = player;

    // You can handle player events here, for example:
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
