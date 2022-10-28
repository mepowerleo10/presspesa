import { useEffect, useState } from 'react';

export const savePersistedState = (key, value) => {
  window.localStorage.setItem(key, JSON.stringify(value));
};

const usePersistedState = (key, defaultValue) => {
  const [value, setValue] = useState(() => {
    const stickyValue = window.localStorage.getItem(key);
    return stickyValue ? JSON.parse(stickyValue) : defaultValue;
  });

  useEffect(() => {
    if (value !== defaultValue) {
      savePersistedState(key, value);
    } else {
      window.localStorage.removeItem(key);
    }
  }, [defaultValue, key, value]);

  return [value, setValue];
};

export default usePersistedState;