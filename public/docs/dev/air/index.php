<html>
    <head>
        <meta charset="utf-8" />
        <meta content="width=device-width,initial-scale=1" name="viewport" />
        <style>
            body {
                font-family: Ubuntu, sans-serif
            }
            .box {
                height: 20vh;
                border: solid 3px gray;
                margin: 5px;
                padding: 5px;
                border-radius: 8px;
            }
            .left {
                font-size: 4vh;
            }
            .right {
                padding-left: 20vw;
            }
            .value {
                font-size: 10vh;
                font-weight: bold;
            }
            .suffix {
                font-size: 5vh;
            }
        </style>
    </head>
    <body>
        <?php
            function row2format($row) {
                $out = [
                    'show' => false,
                    'tmp' => $row->value_type
                ];
                switch ($row->value_type) {
                    case 'SDS_P1':
                        $out = [
                            'show' => true,
                            'formatted_value' => round((float) $row->value),
                            'name' => 'PM<sub>10</sub>',
                            'suffix' => 'μg/m<sup>3</sup>'
                        ];
                        break;
                    case 'SDS_P2':
                        $out = [
                            'show' => true,
                            'formatted_value' => round((float) $row->value),
                            'name' => 'PM<sub>2.5</sub>',
                            'suffix' => 'μg/m<sup>3</sup>'
                        ];
                        break;
                    case 'temperature':
                        $out = [
                            'show' => true,
                            'formatted_value' => round((float) $row->value * 10) / 10,
                            'name' => 'Temperature',
                            'suffix' => '°C'
                        ];
                        break;
                    case 'humidity':
                        $out = [
                            'show' => true,
                            'formatted_value' => round((float) $row->value),
                            'name' => 'Humidity',
                            'suffix' => '%'
                        ];
                        break;
                }
                return $out;          
            }
            function div($r) {
                $out = '<div class="box">' . "\n";
                $out .= '<div class="left">' . "\n";
                $out .= '<span class="name">' . $r['name'] . ':</span>' . "\n";
                $out .= '</div>' . "\n";
                $out .= '<div class="right">' . "\n";
                $out .= '<span class="value">' . $r['formatted_value'] . '</span>' . "\n";
                $out .= '<span class="suffix">' . $r['suffix'] . '</span>' . "\n";
                $out .= '</div>' . "\n";
                $out .= '</div>' . "\n\n";
                return $out;
            }

            $file = "/home/projects/skop.eu/public/docs/dev/air/data.json";
            $data = json_decode(file_get_contents($file));
            $date = filectime($file);
            foreach ($data->sensordatavalues as $row) {
                $r = row2format($row);
                if ($r['show']) {
                    echo div($r);
                } 
            }
            echo "Last measurement: " . date("F d Y H:i:s", $date) . ' (GMT)';
        ?>
    </body>
</html>
