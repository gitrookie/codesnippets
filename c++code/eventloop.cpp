void App::exec() {
  for(;;) {
    vector<Waitable> waitables;
    waitables.push_back(m_networkSocket);
    waitables.push_back(m_xConnection);
    waitables.push_back(m_globalTimer);
    Waitable* whatHappened = System::waitOnAll(waitables);
    switch(whatHappened) {
    case &m_networkSocket: readAndDispatchNetworkEvent(); break;
    case &m_xConnection: readAndDispatchGuiEvent(); break;
    case &m_globalTimer: readAndDispatchTimerEvent(); break;
    }
  }
}

/* Waitable is system dependent. On Unix its called a file descriptor and
   "waitOnAll" is the select system call. The so-called vector<Waitable> is a
   fd-set on Unix, and whatHappened is actually queried via FD_ISSET. The actual
   waitable handles are acquired in various ways, for example m_xConnection can
   taken from XConnectionNumber. X11 also provides a high level portable API
   for this XNextEvent() but if you were to use that, you wouldn't be able to
   several event sources simultaneously.*/
