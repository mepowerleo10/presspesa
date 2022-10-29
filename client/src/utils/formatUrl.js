const baseUrl = "http://127.0.0.1";

export const formatStreamingURL = (uuid) => `${baseUrl}/streaming/processed/${uuid}/dash.mpd`;

export const formatAPIURL = (path, uuid) => `${baseUrl}:8001/api/ads/${path ? path + "/" : ""}${uuid ? uuid : ""}`;