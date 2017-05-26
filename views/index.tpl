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
            <div class="panel-body">
                {{ctime(response.tx_time)}}
            </div>
        </div>

        <div class="panel panel-primary">
            <div class="panel-heading">
                <h2 class="panel-title">Debug Information</h3>
            </div>
            <div class="panel-body">
                {{response.offset}}
            </div>
        </div>
    </div>
</div>
% include('footer.tpl')