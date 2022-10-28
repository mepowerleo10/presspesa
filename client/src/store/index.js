import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { sessionReducer as session } from "./session";
import { errorsReducer as errors } from "./errors";
import { registrationReducer as registration } from "./registration";

const reducer = combineReducers({
  session,
  errors,
  registration,
});

export { sessionActions } from "./session";
export { errorsActions } from "./errors";
export { registrationActions } from "./registration";

export default configureStore({
  reducer,
});
