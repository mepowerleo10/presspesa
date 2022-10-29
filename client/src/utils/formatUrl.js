// const baseUrl = "http://127.0.0.1";
const baseUrl = "http://app.thought.ninja";

export const formatStreamingURL = (uuid) => `${baseUrl}/streaming/processed/${uuid}/dash.mpd`;

export const formatAPIURL = (path, uuid) => `${baseUrl}:8000/api/ads/${path ? path + "/" : ""}${uuid ? uuid : ""}`;