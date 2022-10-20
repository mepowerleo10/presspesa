const { createSlice } = require("@reduxjs/toolkit");

const { reducer, actions } = createSlice({
  name: "session",
  initialState: {
    user: null,
    partialRegistration: false,
  },
  reducers: {
    updateUser(state, action) {
      state.user = action.payload;
    },
    updatePartialRegistration(state, action) {
      state.partialRegistration = action.payload;
    },
  },
});

export { actions as sessionActions };
export { reducer as sessionReducer };
