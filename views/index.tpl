% include('header.tpl')
% from time import ctime
<div class="container">
    <div class="starter-template">
        <h1>Welcome to ntp-viewer</h1>
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
                        <strong>Offset:</strong> {{response.offset}}<br />
                        <strong>Delay:</strong> {{response.delay}}<br />
                        <strong>Precision:</strong> {{response.precision}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
% include('footer.tpl')