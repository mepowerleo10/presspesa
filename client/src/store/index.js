import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { sessionReducer as session } from "./session";
import { errorsReducer as errors } from "./errors";
import { watchedReducer as watched } from "./watched";
import { registrationReducer as registration } from "./registration";

const reducer = combineReducers({
  session,
  errors,
  watched,
  registration,
});

export { sessionActions } from "./session";
export { errorsActions } from "./errors";
export { watchedActions } from "./watched";
export { registrationActions } from "./registration";

export default configureStore({
  reducer,
});
