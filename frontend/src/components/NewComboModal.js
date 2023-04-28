import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewComboForm from "./NewComboForm";

class NewComboModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Edit Combo";
    var button = <Button onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Add Combo to List";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Create New
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle} size="xl">
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>
          <ModalBody>
            <NewComboForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              combo={this.props.combo}
              create={this.props.create}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewComboModal;