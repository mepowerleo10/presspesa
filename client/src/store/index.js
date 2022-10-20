import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { sessionReducer as session } from "./session";
import { errorReducer as error } from "./errors";
import { registrationReducer as registration } from "./registration";

const reducer = combineReducers({
  session,
  error,
  registration,
});

export { sessionActions } from "./session";
export { errorActions } from "./errors";
export { registrationActions } from "./registration";

export default configureStore({
  reducer,
});
