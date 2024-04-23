import React from 'react';
import './Input_Field.css';

function InputField (props) {
  return (
    <div className='input-field-div'>
      <label className='input-field-label'>{props.label}</label>
      <input className='input-field' id={props.value} title={props.value} type={props.value} onChange={props.onChange}/>
    </div>
  );
};

export default InputField;
