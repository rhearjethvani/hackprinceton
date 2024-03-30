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
          <MediaRecorderComponent/>
        </div>


      </header>
    </div>
  );



  /**
   * return (
    <div className="flex flex-col grow px-5 max-md:mt-5 max-md:max-w-full">
      <div className="self-start text-3xl font-bold tracking-wide leading-10 text-blue-950">
        Good morning,
      </div>
      <div className="self-start mt-1.5 text-xl leading-8 text-black">
        Mr. ABC
      </div>
      <div className="px-6 py-6 mt-12 bg-white rounded-xl shadow-sm max-md:pr-5 max-md:mt-10 max-md:max-w-full">
        <div className="flex gap-5 max-md:flex-col max-md:gap-0">
          <div className="flex flex-col w-[63%] max-md:ml-0 max-md:w-full">
            <div className="flex flex-col grow max-md:mt-10 max-md:max-w-full">
              <div className="text-2xl font-semibold tracking-wide leading-7 text-zinc-800 max-md:max-w-full">
                Recent test results
              </div>
              <div className="flex gap-0 self-end mt-12 max-w-full text-xs leading-5 text-black w-[382px] max-md:mt-10">
                <img
                  loading="lazy"
                  src="https://cdn.builder.io/api/v1/image/assets/TEMP/00d5da2f757324dfeea5a6a6bf425c34ce62ca1e3f68d5aaab49e3181ae24460?apiKey=de307d3e80fe4c8cab38ccbf88c12763&"
                  className="grow shrink-0 aspect-square basis-0 w-fit"
                />
                <div className="justify-center self-start px-2 py-px mt-16 bg-white rounded-xl border-solid shadow border-[0.5px] border-zinc-800 max-md:mt-10">
                  19% passing with A grade
                </div>
              </div>
              <div className="flex gap-5 justify-between mt-5 max-md:flex-wrap">
                <div className="flex flex-col">
                  <div className="self-center text-2xl font-bold tracking-wide leading-7 text-blue-950">
                    1381
                  </div>
                  <div className="mt-1.5 text-sm leading-5 text-black">
                    Students attended the test
                  </div>
                </div>
                <div className="flex flex-col">
                  <div className="self-center text-2xl font-bold tracking-wide leading-7 text-blue-950">
                    92
                  </div>
                  <div className="mt-1.5 text-sm leading-5 text-black">
                    Students didn’t attend the test
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="flex flex-col ml-5 w-[37%] max-md:ml-0 max-md:w-full">
            <div className="flex flex-col grow mt-16 leading-[150%] max-md:mt-10">
              <div className="flex flex-col items-start pl-8 max-md:pl-5">
                <div className="text-base text-black">220 students</div>
                <div className="mt-1.5 text-sm text-neutral-500">
                  19% Students passing with A grade
                </div>
              </div>
              <div className="flex flex-col items-start pl-8 mt-6 max-md:pl-5">
                <div className="text-base text-black">220 students</div>
                <div className="mt-1.5 text-sm text-neutral-500">
                  19% Students passing with B grade
                </div>
              </div>
              <div className="flex flex-col items-start pl-8 mt-6 max-md:pl-5">
                <div className="text-base text-black">220 students</div>
                <div className="mt-1.5 text-sm text-neutral-500">
                  19% Students passing with C grade
                </div>
              </div>
              <div className="flex flex-col items-start pl-8 mt-6 max-md:pl-5">
                <div className="text-base text-black">220 students</div>
                <div className="mt-1.5 text-sm text-neutral-500">
                  19% Students passing with D grade
                </div>
              </div>
              <div className="flex flex-col items-start pl-9 mt-6 max-md:pl-5">
                <div className="text-base text-black">220 students</div>
                <div className="mt-1.5 text-sm text-neutral-500">
                  19% Students failing the test
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="flex flex-col p-5 mt-5 bg-white rounded-xl shadow-sm max-md:max-w-full">
        <div className="text-2xl font-semibold leading-7 text-black max-md:max-w-full">
          Overall survey
        </div>
        <div className="flex gap-0.5 mt-11 max-md:flex-wrap max-md:mt-10">
          <div className="flex flex-col self-start text-lg leading-7 whitespace-nowrap text-stone-300">
            <div>1500</div>
            <div className="mt-10">1200</div>
            <div className="mt-10">900</div>
            <div className="mt-10">600</div>
            <div className="mt-10">300</div>
          </div>
          <div className="flex flex-col grow shrink-0 basis-0 w-fit max-md:max-w-full">
            <div className="flex gap-5 justify-between items-end self-end max-w-full w-[683px] max-md:flex-wrap max-md:mr-2.5">
              <div className="shrink-0 mt-8 h-[258px] rounded-[37px_37px_0px_0px] w-[50px]" />
              <div className="shrink-0 mt-20 h-[212px] rounded-[37px_37px_0px_0px] w-[50px] max-md:mt-10" />
              <div className="shrink-0 mt-56 h-[71px] rounded-[37px_37px_0px_0px] w-[50px] max-md:mt-10" />
              <div className="shrink-0 self-stretch h-[291px] rounded-[37px_37px_0px_0px] w-[50px]" />
              <div className="shrink-0 mt-16 h-[226px] rounded-[37px_37px_0px_0px] w-[50px] max-md:mt-10" />
            </div>
            <div className="shrink-0 h-0.5 bg-black border-2 border-black border-solid max-md:max-w-full" />
            <div className="flex flex-col pl-8 mt-2 max-md:pl-5 max-md:max-w-full">
              <div className="flex gap-5 justify-between text-base leading-6 whitespace-nowrap text-stone-300 max-md:flex-wrap max-md:max-w-full">
                <div>Weekly</div>
                <div>Quizes</div>
                <div>Questionnairs</div>
                <div>Monthly</div>
                <div>Practice</div>
              </div>
              <div className="flex gap-4 self-end mt-8">
                <div className="text-base tracking-normal leading-6 text-neutral-500">
                  Overall students attending the tests
                </div>
                <div className="text-lg font-bold tracking-wide leading-7 text-zinc-800">
                  Yearly
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
   */
}

export default App;
