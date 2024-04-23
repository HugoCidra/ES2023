import React from 'react';
import '../index.css';
import DataFetchGet from '../../DataFetchFunctions/DataFetchGet';
import './Profile.css';
import NavBar from '.././NavBar/NavBar';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Legend, Tooltip, ResponsiveContainer, ReferenceLine} from 'recharts';

const fixedContainerStyle = {
    position: 'fixed',
    top: '100px',
    left: '25%',
    transform: 'translateX(-50%)',
    width: '700px',
    height: '400px',
    zIndex: 10,
};


const fixedContainerStyle2 = {
    position: 'fixed',
    top: '100px',
    left: '75%',
    transform: 'translateX(-50%)',
    width: '700px',
    height: '400px',
    zIndex: 10,
};


class CreatorChart extends React.Component {



    /**
     * Constructor for CreatorChart Component
     * @param {state} state Variable which holds information which may change during lifetime of this component
     * @param {Array} data An array containing the data of the user
     *  @param {boolean} loading A boolean flag, initialized to true, representing the initial loading state of the component. It's used to control the rendering of the component while waiting for data to be fetched.
     */
    constructor() {
        super();
        this.state = {
            data: [],
            is_solver: 0,
            loading: true,
        };
    }

    /**
     * Lifecycle method of React component, called after the component mounts.
     * This method performs two main tasks:
     * 1. Fetches data related to the tags of the user. It assumes the user is a creator and makes an API call to get the user's creator tags.
     * 2. Simultaneously, it fetches data to determine the user's status (solver or creator) by making another API call.
     *
     * Both API calls are made in parallel using Promise.all for efficiency.
     *
     * Once the data is successfully fetched:
     *   - The creator's tag data is stored in the 'data' state.
     *   - The user's status as a solver or creator is determined based on the response status. If the status is not 401, the user is considered a solver.
     *   - The solver data, if available, is stored in the 'solverData' state.
     *   - The 'loading' state is set to false indicating that the data fetching is complete.
     *
     * In case of any errors during the API calls:
     *   - The error is logged to the console.
     *   - The 'loading' state is set to false to indicate the completion of the data fetching process, even if it ends in error.
     */
    async componentDidMount() {
        try {
            const tagsCreatorPromise = DataFetchGet('api/REQ8/get_tags_creator/', null);
            const statsSolverPromise = DataFetchGet('api/REQ8/get_stats_solver/', null);

            const [response, solverResponse] = await Promise.all([tagsCreatorPromise, statsSolverPromise]);

            this.setState({
                data: response['data'].data,
                is_solver: solverResponse.data.status !== 401 ? 1 : 0,
                solverData: solverResponse.data.status !== 401 ? solverResponse['data'].data : [],
                loading: false,
            });

        } catch (error) {
            console.log("error", error);
            this.setState({ loading: false });
        }
    }




    /**
     * Render function for the CreatorChart component.
     * This function performs the following tasks based on the state of the component:
     * 1. If data is still loading (indicated by the 'loading' state), it returns null, effectively rendering nothing.
     * 2. If there are no quizzes (i.e., the 'data' array is empty), it returns a message indicating that the user has no approved or not approved quizzes.
     * 3. If there are quizzes, it renders a BarChart with the data:
     *    - The BarChart, from the 'recharts' library, displays data using horizontal bars.
     *    - The length of each bar is proportional to the data value it represents, providing a visual representation of the quizzes' data.
     *    - The chart is styled conditionally based on whether the user is a solver (as indicated by the 'is_solver' state).
     *    - Additional chart elements like XAxis, YAxis, Tooltip, and Legend are configured for display.
     *    - Reference lines and tick intervals are calculated and rendered to enhance readability and context of the chart.
     *
     * @returns {JSX Element} - either a loading indicator, a message for no data, or a BarChart with quiz data.
     */
    render(){
        const { data, is_solver, loading } = this.state;
        if (loading) {
            return null;
        }
        if (data.length === 0) {
            return <div className="caixa-texto">You do not have approved or not approved quizzes!</div>;
        } else {
            const maxValue = Math.max(...data.map(d => Math.max(d.x, d.y)));
            const interval = 5;
            const referenceLineValues = Array.from(
                { length: Math.ceil(maxValue / interval) },
                (_, index) => (index + 1) * interval
            );
            const ticks = Array.from({ length: Math.ceil(maxValue / interval) + 1 }, (_, index) => index * interval);

            return (
                <div style={fixedContainerStyle}>
                    <div className="quiz-flag">Quizzes</div>
                    <ResponsiveContainer width="100%" height="100%">
                        <BarChart
                            data={data}
                            layout="horizontal"
                            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                        >
                            <XAxis type="category" dataKey="name" fontFamily="Century Gothic" fontSize={'20px'} color='black' tickLine={false} />
                            <YAxis fontFamily="Century Gothic" type="number" fontSize={'20px'} axisLine={false} tickLine={false} domain={[0, interval * Math.ceil(maxValue / interval)]} ticks={ticks}/>
                            <Tooltip />
                            <Legend verticalAlign="top" height={36} align="center" iconSize="20" formatter={(value, entry) => <span style={{ fontSize: '18px', color:'black'}}>{value}</span>}/>
                            {referenceLineValues.map(value => (
                                <ReferenceLine key={value} y={value} stroke="#CCC" />
                            ))}
                            <Bar name="Approved" dataKey="x" fill="rgb(200,228,196)" barSize={20}/>
                            <Bar name="Not Approved" dataKey="y" fill="rgb(221,189,189)" barSize={20}/>
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            );
        }
    }
}



class SolverChartAnswers extends React.Component{

    /**
     * Constructor for SolverChartAnswers Component.
     * @param {state} state Variable which holds information which may change during lifetime of this component.
     * @param {Array} data An array containing the data of the user.
     * @param {int} is_solver An integer that could be a boolean. 1 is True, everything else is False.
     * @param {boolean} loading A boolean flag, initialized to true, representing the initial loading state of the component. It's used to control the rendering of the component while waiting for data to be fetched.
     */
    constructor() {
        super();
        this.state = {
            data:[],
            is_solver: 1,
            loading: true,
        };
    }

    /**

     * This method is responsible for fetching data related to the solver's statistics and updating the component's state accordingly.
     *
     * The function performs the following tasks:
     *   - Makes an asynchronous API call to fetch solver statistics using DataFetchGet.
     *   - If the response status is 401, indicating  that the user is not a solver, it sets the 'is_solver' state to 0 (false).
     *   - Regardless of the response status, it updates the 'data' state with the fetched data, if available.
     *   - The 'loading' state is set to false after the data fetching is complete or if an error occurs, to indicate that the component has finished loading data.
     *
     * In case of any error during the API call:
     *   - The error is logged to the console.
     *   - The 'loading' state is set to false to signify the end of the data fetching process.
     */
    async componentDidMount() {
        try {
            let response = await DataFetchGet('api/REQ8/get_stats_solver/', null);
            console.log(response);
            if(response.data.status === 401){
                this.setState({is_solver: 0})
            }
            this.setState({data: response['data'].data,loading: false });

        } catch (error) {
            console.log("error", error);
            this.setState({loading: false});
        }
    }

    /**
     * Render function for the SolverChartAnswers component.
     * This function dynamically renders content based on the current state of the component, performing the following tasks:
     *
     * 1. If the component is in the loading state (indicated by 'loading' being true), it returns null, rendering nothing.
     * 2. If the data array is empty (indicating no tests have been solved by the user), it displays a message to the user stating they have not solved any tests yet.
     * 3. If there is data (indicating the user has solved tests), it renders a BarChart with this data:
     *    - The BarChart, imported from the 'recharts' library, uses horizontal bars to represent the data. The length of each bar is proportional to the value it represents.
     *    - The chart includes X and Y axes, tooltips for detailed data points, and a legend for clarity.
     *    - Reference lines are added to the chart for better data visualization. These are calculated based on the maximum value in the data set and a predefined interval.
     *
     * @returns {JSX Element} - The rendered JSX element, which can be either a message div or a BarChart, depending on the component's state.
     */
    render() {
        if (this.state.loading) {
            return null;
        }
        if (this.state.data.length === 0) {
            return (
                <div className="box pergunta caixa-texto" id="profile_msg" style={{
                    fontSize: '18px',
                    marginLeft: '40%',
                    width: 'auto',
                    maxWidth: '50%',
                    padding: '10px',
                    boxSizing: 'border-box',
                    display: 'inline-block'
                }}>
                    You have not solved any test yet!
                </div>
            );
        }

        const maxValue = Math.max(...this.state.data.map(d => Math.max(d.x, d.y)));
        const interval = 5;
        const referenceLineValues = Array.from({ length: Math.ceil(maxValue / interval) }, (_, index) => (index + 1) * interval);
        const ticks = Array.from({ length: Math.ceil(maxValue / interval) + 1 }, (_, index) => index * interval);

        return (
            <div style={fixedContainerStyle2}>
                <div className="quiz-flag">Answers</div>
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart
                        data={this.state.data}
                        margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                    >
                        <XAxis type="category" dataKey="name" fontFamily="Century Gothic" fontSize={'20px'} color='black' tickLine={false} />
                        <YAxis fontFamily="Century Gothic" type="number" fontSize={'20px'} axisLine={false} tickLine={false} domain={[0, interval * Math.ceil(maxValue / interval)]} ticks={ticks}/>
                        <Tooltip />
                        <Legend verticalAlign="top" height={36} align="center" iconSize="20" formatter={(value, entry) => <span style={{ fontSize: '18px', color: 'black' }}>{value}</span>} />
                        {referenceLineValues.map(value => (
                            <ReferenceLine key={`ref-line-${value}`} y={value} stroke="#CCC" />
                        ))}
                        <Bar name="Correct" dataKey="x" fill="rgb(200,228,196)" barSize={20} />
                        <Bar name="Not Correct" dataKey="y" fill="rgb(221,189,189)" barSize={20} />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        );
    }
}

class Profile extends React.Component {
    constructor(props) {
        super(props);
        // Start the state of is_solver, assuming 0 is the norm (non-solver)
        this.state = {
            is_solver: 0,
            loading: true,
        };
    }



    async componentDidMount() {
        //API call to figure out if the user is a solver or a creator

        try{
            let response = await DataFetchGet('api/REQ8/get_stats_solver/', null);
            console.log(response);
            if(response.data.status === 401){
                this.setState({is_solver: 0})
            }

            else{
                this.setState({is_solver:1})
            }
            this.setState({data: response['data'].data, loading:false});

        }


        catch (error) {
            console.log("error", error);
        }
    }

    render() {
        const { is_solver, loading } = this.state;
        if (loading) {
            return null;
        }

// Style for the container of the charts and titles
// Sets up a flexible layout with horizontal alignment.
// 'justifyContent: center' centers items along the main axis (horizontally),
// while 'alignItems: flex-start' aligns items to the start of the cross axis (vertically).
        const chartContainerStyle = {
            display: "flex",
            flexDirection: 'row',
            justifyContent: 'center',
            alignItems: 'flex-start',
        };

// Style for the individual containers of the charts and their titles
// 'alignItems: center' centers items along the cross axis (vertically).
// 'margin: 0 -400px' applies a negative margin, which can be used for positioning adjustments.
// 'flex: 1' allows the container to occupy all available space in the flex line.
        const individualChartStyle = {
            alignItems: 'center',
            margin: '0 -400px',
            flex: '1',
        };

// Style to center the CreatorChart when there are no SolverChartAnswers

        const centeredChartStyle = {
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            height: '80vh',
            width: '100%',
        };





        return (
            <main>
                <div className="container-background">
                    <NavBar/>
                    {/* Render CreatorChart with centeredChartStyle if user is not a solver */}
                    {is_solver === 0 && (
                        <div style={centeredChartStyle}>
                            <CreatorChart />
                        </div>
                    )}

                    {/* Render both graphs side by side with chartContainerStyle if user is a solver */}
                    {is_solver === 1 && (
                        <div style={chartContainerStyle}>
                            <div style={individualChartStyle}>

                                <CreatorChart />
                            </div>
                            <div style={individualChartStyle}>
                                <SolverChartAnswers />
                            </div>
                        </div>
                    )}
                </div>
            </main>
        );
    }
}

export default Profile;
