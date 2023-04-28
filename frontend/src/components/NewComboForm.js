import React from "react";
import { Button, Col, Container, Form, FormGroup, Input, Label, Row } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";
import Switch from "react-switch";
import FilePreviewer from "./FilePreviewer";
import Select from 'react-select';

const locationOptions = [
  {
    label: "Anywhere",
    value: "ANY"
  },
  {
    label: "Midscreen",
    value: "MID"
  },
  {
    label: "Corner",
    value: "COR"
  }
];

class NewComboForm extends React.Component {
  state = {
    pk: 0,
    comboNotation: "",
    damage: 0,
    meterCost: 0,
    moonSkillCost: 0,
    moonDrive: false,
    meterGain: 0,
    location: "",
    notes: "",
    videoFile: ""
  };

  componentDidMount() {
    if (this.props.combo) {
      const { pk, comboNotation, damage, meterCost, moonSkillCost, moonDrive, meterGain, location, notes, videoFile } = this.props.combo;
      this.setState({ pk, comboNotation, damage, meterCost, moonSkillCost, moonDrive, meterGain, location, notes, videoFile });
      this.locationConstructor(location)
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  locationConstructor(givenLocation) {
    locationOptions.forEach(option => {
      if (option.value == givenLocation) {
        this.setState({
          location: {
            label: option.label,
            value: option.value,
          }
        })
      }
    });
  }

  onLocationChange = e => {
    this.setState({
      location: {
        label: e.label,
        value: e.value,
      }
    })
  }

  onSwitchChange = e => {
    this.setState({
      moonDrive: !this.state.moonDrive
    })
  }

  createCombo = e => {
    console.log("UPLOADING COMBO")
    console.log(this.state.comboNotation)
    e.preventDefault();
    var data;
    if (this.state.videoFile == "") {
      data = JSON.stringify({
        damage: parseInt(this.state.damage),
        comboNotation: this.state.comboNotation,
        meterCost: parseInt(this.state.meterCost),
        moonSkillCost: parseInt(this.state.moonSkillCost),
        moonDrive: this.state.moonDrive,
        meterGain: parseInt(this.state.meterGain),
        location: this.state.location.value,
        notes: this.state.notes,
      });
    } else {
      data = JSON.stringify({
        damage: parseInt(this.state.damage),
        comboNotation: "asd",
        meterCost: parseInt(this.state.meterCost),
        moonSkillCost: parseInt(this.state.moonSkillCost),
        moonDrive: this.state.moonDrive,
        meterGain: parseInt(this.state.meterGain),
        location: this.state.location.value,
        notes: this.state.notes,
        videoFile: this.state.videoFile,
      });
    }

    axios.post(API_URL, data, {
      headers: {
        'Access-Control-Allow-Origin': true,
        'Content-Type': 'application/json'
      },
      mode: 'cors',
    })
      .then(() => {
        this.props.resetState();
        this.props.toggle();
      })
      .catch((err) => {
        console.log("Response Received: ", err.response)
        console.log("AXIOS ERROR: ", err)
        console.log("With Data: ", data)
      });
  };

  editCombo = e => {
    e.preventDefault();
    var data = [{
      damage: parseInt(this.state.damage),
      comboNotation: this.state.comboNotation,
      meterCost: parseInt(this.state.meterCost),
      moonSkillCost: parseInt(this.state.moonSkillCost),
      moonDrive: this.state.moonDrive,
      meterGain: parseInt(this.state.meterGain),
      location: this.state.location.value,
      notes: this.state.notes,
      videoFile: this.state.videoFile,
    }]
    axios.put(API_URL + this.state.pk, data, {
      headers: {
        'Access-Control-Allow-Origin': true,
        'Content-Type': 'application/json'
      },
      mode: 'cors',
    })
      .then(() => {
        this.props.resetState();
        this.props.toggle();
      });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.combo ? this.editCombo : this.createCombo}>
        <Container>
          <Row>
            <Col>
              <FormGroup>
                <Label for="comboNotation">Combo:</Label>
                <textarea class="w-100 border-2 rounded form-control"
                  name="comboNotation"
                  onChange={this.onChange}
                  value={this.defaultIfEmpty(this.state.comboNotation)}
                />
              </FormGroup>
            </Col>
          </Row>
          <Row>
            <Col>
              <FormGroup>
                <Label for="damage">Damage:</Label>
                <Input name="damage" type="number" min="0" max="12300" onChange={this.onChange}
                  value={this.defaultIfEmpty(this.state.damage)}></Input>
              </FormGroup>
            </Col>
            <Col>
              <FormGroup>
                <Label for="meterCost">Meter Cost:</Label>
                <Input name="meterCost" type="number" min="0" max="4" onChange={this.onChange}
                  value={this.defaultIfEmpty(this.state.meterCost)}></Input>
              </FormGroup>
            </Col>
            <Col>
              <FormGroup>
                <Label for="meterGain">Meter Gain:</Label>
                <Input name="meterGain" type="number" min="0" max="4" onChange={this.onChange}
                  value={this.defaultIfEmpty(this.state.meterGain)}></Input>
              </FormGroup>
            </Col>
          </Row>
          <Row>
            <Col>
              <FormGroup>
                <Label for="moonSkillCost">Moon Skill Cost:</Label>
                <Input name="moonSkillCost" type="number" min="0" max="6" onChange={this.onChange}
                  value={this.defaultIfEmpty(this.state.moonSkillCost)}></Input>
              </FormGroup>
            </Col>
            <Col>
              <FormGroup>
                <Container>
                  <Row>
                    <Col>
                      <Label for="moonDrive">Moon Drive:</Label>
                    </Col>
                  </Row>
                  <Row>
                    <Col>
                      <Switch name="moonDrive"
                        onChange={this.onSwitchChange}
                        checked={this.state.moonDrive}
                      ></Switch>
                    </Col>
                  </Row>
                </Container>
              </FormGroup>
            </Col>
            <Col>
              <FormGroup>
                <Label for="location">Location:</Label>
                <Select name="location" options={locationOptions} value={this.state.location != "" ? this.state.location : locationOptions[0]} onChange={this.onLocationChange}>
                </Select>
              </FormGroup>
            </Col>
          </Row>
          <Row>
            <Col>
              <FormGroup>
                <Label for="notes">Notes:</Label>
                <textarea
                  name="notes"
                  onChange={this.onChange}
                  value={this.defaultIfEmpty(this.state.notes)}
                />
              </FormGroup>
            </Col>
            <Col>
              <FormGroup>
                <Label for="video">Video:</Label>
                <FilePreviewer />
              </FormGroup>
            </Col>
          </Row>
        </Container>
        <Button onClick={this.props.create == true ? this.createCombo : this.editCombo}>{this.props.create == true ? 'Upload' : 'Update Combo'}</Button>
      </Form>
    );
  }
}

export default NewComboForm;