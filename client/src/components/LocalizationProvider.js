import React, {
    createContext, useContext, useEffect, useMemo,
  } from 'react';
  import moment from 'moment';
  import 'moment/min/locales.min';
  
  import en from '../resources/l10n/en.json';
  import sw from '../resources/l10n/sw.json';
  import usePersistedState from 'src/utils/usePersistedState';
  
  const languages = {
    en: { data: en, name: 'English', icon: "/static/icons/ic_flag_uk.svg", },
    sw: { data: sw, name: 'Swahili', icon: "/static/icons/ic_flag_tz.svg" },
  };
  
  const getDefaultLanguage = () => {
    const browserLanguages = window.navigator.languages ? window.navigator.languages.slice() : [];
    const browserLanguage = window.navigator.userLanguage || window.navigator.language;
    browserLanguages.push(browserLanguage);
    browserLanguages.push(browserLanguage.substring(0, 2));
  
    for (let i = 0; i < browserLanguages.length; i += 1) {
      let language = browserLanguages[i].replace('-', '');
      if (language in languages) {
        return language;
      }
      if (language.length > 2) {
        language = language.substring(0, 2);
        if (language in languages) {
          return language;
        }
      }
    }
    return 'en';
  };
  
  const LocalizationContext = createContext({
    languages,
    language: 'en',
    setLanguage: () => {},
  });
  
  export const LocalizationProvider = ({ children }) => {
    const [language, setLanguage] = usePersistedState('language', getDefaultLanguage());
  
    const value = useMemo(() => ({ languages, language, setLanguage }), [language, setLanguage]);
  
    useEffect(() => {
      let selected;
      if (language.length > 2) {
        selected = `${language.slice(0, 2)}-${language.slice(-2).toLowerCase()}`;
      } else {
        selected = language;
      }
      moment.locale([selected, 'en']);
    }, [language]);
  
    return (
      <LocalizationContext.Provider value={value}>
        {children}
      </LocalizationContext.Provider>
    );
  };
  
  export const useLocalization = () => useContext(LocalizationContext);
  
  export const useTranslation = () => {
    const context = useContext(LocalizationContext);
    const { data } = context.languages[context.language];
    return useMemo(() => (key) => data[key], [data]);
  };
  
  export const useTranslationKeys = (predicate) => {
    const context = useContext(LocalizationContext);
    const { data } = context.languages[context.language];
    return Object.keys(data).filter(predicate);
  };