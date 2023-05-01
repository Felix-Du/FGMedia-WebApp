import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ComboList from "./ComboList";
import NewComboModal from "./NewComboModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    combos: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCombos = () => {
    axios.get(API_URL).then(res => this.setState({ combos: res.data }));
  };

  resetState = () => {
    this.getCombos();
  };

  render() {
    return (
      <Container fluid style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <ComboList
              combos={this.state.combos}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewComboModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;