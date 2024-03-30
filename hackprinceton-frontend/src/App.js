import logo from './logo.svg';
import './App.css';
import MediaRecorderComponent from './MediaRecorder';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Hello World!</p>

        <div>
          <h2>Question for the User</h2>
          <p>What do you want to record today?</p>
        </div>

        <div>
          <h2>Record Video Software</h2>
          <p>This is where you can embed your record video software.</p>
        </div>

        <div>
          <MediaRecorderComponent />
        </div>


      </header>
    </div>
  );

}

export default App;