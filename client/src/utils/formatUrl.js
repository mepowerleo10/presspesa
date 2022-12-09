export const formatStreamingURL = (uuid) => `/streaming/processed/${uuid}/dash.mpd`;

export const formatAPIURL = (path, uuid) => `/api/ads/${path ? path + "/" : ""}${uuid ? uuid : ""}`;