import React from "react";


const RadioButton = (props) => {
    return (
        <div className="column">
            <input id={props.id} onChange={props.changed} value={props.value} type="radio" checked={props.isSelected} disabled={props.disabled} />
            <label className={props.classe} htmlFor={props.id}>{props.label}</label>
        </div>
    );
}

export default RadioButton;