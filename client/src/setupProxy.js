const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/api",
    createProxyMiddleware({
      target: `http://${process.env.REACT_APP_URL_NAME}`,
      changeOrigin: true,
    })
  );
  app.use(
    "/streaming",
    createProxyMiddleware({
      target: `http://${process.env.REACT_APP_STREAMING_URL_NAME}`,
      changeOrigin: true,
    })
  );
};
