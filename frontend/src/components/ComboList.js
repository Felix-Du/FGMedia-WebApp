import React, { Component } from "react";
import { Table } from "reactstrap";
import NewComboModal from "./NewComboModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class ComboList extends Component {
    render() {
        const combos = this.props.combos;
        return (
            <Table dark>
                <thead>
                    <tr>
                        <th>Combo Notation</th>
                        <th>Damage</th>
                        <th>Meter Cost (Bars)</th>
                        <th>Moon Skill Cost</th>
                        <th>Moon Drive</th>
                        <th>Meter Gain</th>
                        <th>Location</th>
                        <th>Notes</th>
                        <th>Video</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {!combos || combos.length <= 0 ? (
                        <tr>
                            <td colSpan="6" align="center">
                                <b>No Combos Uploaded Yet.</b>
                            </td>
                        </tr>
                    ) : (
                        combos.map(combo => (
                            <tr key={combo.pk}>
                                <td>{combo.comboNotation}</td>
                                <td>{combo.damage}</td>
                                <td>{combo.meterCost}</td>
                                <td>{combo.moonSkillCost}</td>
                                <td>{combo.moonDrive == true ? 'O' : 'X'}</td>
                                <td>{combo.meterGain}</td>
                                <td>
                                    {combo.location == 'ANY' ? 'Anywhere' :
                                        combo.location == 'MID' ? 'Midscreen Only' :
                                            combo.location == 'COR' ? 'Corner Only' :
                                                ''}
                                </td>
                                <td>{combo.notes}</td>
                                <td><video width='400' controls>
                                    <source src={combo.videoFile} type='video/mp4' />
                                    Your browser does not support the video tag.
                                </video></td>
                                <td align="center">
                                    <NewComboModal
                                        create={false}
                                        combo={combo}
                                        resetState={this.props.resetState}
                                    />
                                    &nbsp;&nbsp;
                                    <ConfirmRemovalModal
                                        pk={combo.pk}
                                        resetState={this.props.resetState}
                                    />
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </Table>
        );
    }
}

export default ComboList;