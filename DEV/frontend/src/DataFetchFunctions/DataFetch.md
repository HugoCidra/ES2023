# DataFetch Functions
## Necessary modules: **Axios**
## Functions for three HTTP methods:
- get
- post
- put

**Read information of each function in source code**
## Concrete example of how to use the functions
```
import React, { Component } from 'react'
import DataFetchGet from './DataFetchFunctions/DataFetchGet';
class TestView extends Component{
    async button_refresh(){
        let result=await DataFetchGet('api/REQ2/creators/')
        console.log(result)
    }
    render(){
        return(
            <div>
            <h1>TEST</h1>
            <button onClick={this.button_refresh}>REFRESH</button>
            </div>
        );
    }
}

const Test = () => {
    return (
        <>  
            <main>
                <TestView/>
            </main>
        </>
    );
}

export default Test;
```