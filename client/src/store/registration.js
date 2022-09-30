const { createSlice } = require("@reduxjs/toolkit");

const { reducer, actions } = createSlice({
  name: "session",
  initialState: {
    user: null,
  },
  reducers: {
    updateUser(state, action) {
      state.user = action.payload;
    },
  },
});

export { actions as registrationActions };
export { reducer as registrationReducer };
