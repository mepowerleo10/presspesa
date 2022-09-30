import PropTypes from 'prop-types';
// form
import { useFormContext, Controller } from 'react-hook-form';
// @mui
import { InputAdornment, TextField } from '@mui/material';

// ----------------------------------------------------------------------

RHFPhoneField.propTypes = {
  name: PropTypes.string,
};

export default function RHFPhoneField({ name, ...other }) {
  const { control } = useFormContext();

  return (
    <Controller
      name={name}
      control={control}
      render={({ field, fieldState: { error } }) => (
        <TextField
          {...field}
          InputProps={{
            startAdornment: <InputAdornment position="start">255</InputAdornment>,
          }}
          fullWidth
          type={'tel'}
          value={field.value}
          error={!!error}
          helperText={error?.message}
          {...other}
        />
      )}
    />
  );
}
