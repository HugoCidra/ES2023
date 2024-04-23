import React from "react";
import "./MenuModal.css";
import Admin from "../Admin/Admin";

export default function MenuModal({ modal, toggleModal }) {


  React.useEffect(() => {
    if (modal) {
      document.body.classList.add('active-modal');
    } else {
      document.body.classList.remove('active-modal');
    }
  }, [modal]); 

  return (
    <>
      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay"></div>
            <Admin/>
        </div>
      )}
    </>
  );
}