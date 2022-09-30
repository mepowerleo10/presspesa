import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { sessionReducer as session } from "./session";

const reducer = combineReducers({
  session,
});

export { sessionActions } from "./session";

export default configureStore({
  reducer,
});
