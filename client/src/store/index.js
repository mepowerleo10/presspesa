import { combineReducers, configureStore } from "@reduxjs/toolkit";

import { sessionReducer as session } from "./session";
import { errorReducer as error } from "./errors";

const reducer = combineReducers({
  session,
  error,
});

export { sessionActions } from "./session";
export { errorActions } from "./errors";

export default configureStore({
  reducer,
});
