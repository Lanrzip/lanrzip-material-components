/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { LanrzipMaterialComponents, MuiButton, MuiTextField } from '../lib';

const App = () => {

    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <LanrzipMaterialComponents
                setProps={setProps}
                {...state}
            />
            <MuiButton
                setProps={setProps}
                variant='contained'
            />
            <MuiTextField
                
            />
        </div>
    )
};


export default App;
