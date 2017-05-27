% include('header.tpl')
% from time import ctime
<div class="container">
    <div class="starter-template">
        <h1>Welcome to ntp-viewer</h1>
        <p class="lead">
            Running on {{host}}
        </p>
        <p>&nbsp;</p>

        <div class="panel panel-primary">
            <div class="panel-heading">
                <h2 class="panel-title">Current Time</h3>
            </div>
            <div class="panel-body" id="timestamp">
                {{ctime(response.tx_time)}} UTC
            </div>
        </div>

        <div class="panel panel-primary">
            <div class="panel-heading">
                <h2 class="panel-title">Debug Information</h3>
            </div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-md-6">
                        <strong>Stratum:</strong> {{response.stratum}}<br />
                        <strong>Version:</strong> {{response.version}}<br />
                        <strong>Mode:</strong> {{response.mode}}
                    </div>
                    <div class="col-md-6">
                        <strong>Offset:</strong><p id="offset">{{format(response.offset, '.15f')}}s</p>
                        <strong>Delay:</strong><p id="delay">{{format(response.delay, '.15f')}}s</p>
                        <p><strong>Precision:</strong>{{response.precision}}</p>
                    </div>
                </div>
                <small>Data is refreshed every 10 seconds</small>
            </div>
        </div>
    </div>
</div>
% include('footer.tpl')