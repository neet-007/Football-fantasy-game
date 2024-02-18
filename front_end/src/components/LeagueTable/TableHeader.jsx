import React from 'react'
import Tr from '../shared/Tr/Tr';
import Th from '../shared/Th/Th';


function TableHeader() {
  return (
        <Tr className={'d-flex gap-1 width-100 cap'}>
        <Th>
            <p>
            pos
            </p>
        </Th>
        <Th className={'f-basis-30 d-flex justify-content-start'}>
            club
        </Th>
        <Th>
          pl
        </Th>
        <Th>
          w
        </Th>
        <Th>
          d
        </Th>
        <Th>
          l
        </Th>
        <Th>
          gd
        </Th>
        <Th className={'f-basis-20 d-flex justify-content-center'}>
            form
        </Th>
        <Th>
          pts
        </Th>
        <Th>
          next
        </Th>
      </Tr>
  );
}

export default TableHeader;
